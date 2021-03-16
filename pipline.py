from Structure.EVM import EVM,EVM_stack,EVM_memory,EVM_storage

import os
import json
import logging
import pandas as pd
import math

from Structure.Constant import OPCODE_TO_INSTR
from Structure.Transaction import Transaction
from Structure.utils import disassemble

def execute_init(transaction:'Transaction'):
    contract_hex = transaction.get("msg_input")
    if contract_hex.startswith("0x"):
        contract_hex = contract_hex[2:]
    hex_split = contract_hex.index(contract_hex[:8],2)

    init_hex = contract_hex[:hex_split]
    opcodes = disassemble(init_hex)

    evm = EVM(
        Stack=EVM_stack(),
        Memory=EVM_memory(),
        Storage=EVM_storage({}),
        Transaction=transaction
    )
    while True:
        opcode = opcodes[evm.pc][0]
        args = opcodes[evm.pc][1]

        if opcode in ["RETURN","STOP","REVERT"]:
            break
        evm.pc += 1
        if args is not None:
            args_bytes = int(opcode.lstrip("PUSH"))
            evm.pc += args_bytes

        evm.args = args
        eval_function = "evm.%s()"%opcode        
        eval(eval_function)
    
    run_hex = contract_hex[hex_split:]
    run_opcodes = disassemble(run_hex)

    return run_opcodes, evm.Storage

def execute_tx(storage:'EVM_storage',transaction:'Transaction',opcodes:'Dict',DEBUG_Point:int=0x0,verbose:bool=False):
    evm = EVM(
        Stack=EVM_stack(),
        Memory=EVM_memory(),
        Storage=storage,
        Transaction=transaction
    )
    tx_hash = transaction.get("tx_hash")
    
    if verbose:
        f = open("./log/running/%s.log"%tx_hash,"w",encoding="utf-8")

    while True:
        opcode = opcodes[evm.pc][0]
        args = opcodes[evm.pc][1]

        if verbose:
            f.write("stack:[%s]\nmemory:%s\nstorage:%s\n%s\n\n"%(str(evm.Stack),str(evm.Memory),str(evm.Storage),"="*10+hex(evm.pc)+"_"+str(evm.pc)+":"+str(opcodes[evm.pc])+"="*10))

        if opcode in ["RETURN","STOP","REVERT"]:
            if opcode == "REVERT":
                raise ValueError("REVERT Happened...")
            break
        evm.pc += 1
        if args is not None:
            args_bytes = int(opcode.lstrip("PUSH"))
            evm.pc += args_bytes

        evm.args = args
        eval_function = "evm.%s()"%opcode        
        eval(eval_function)

    if verbose:
        f.close()
        with open("./log/storage_readwrite/%s.json"%tx_hash,"w",encoding="utf-8") as f:
            json.dump({"read":[v.rjust(64,"0") for v in evm.readStorage],"write":[v.rjust(64,"0") for v in evm.writeStorage]},f,indent='\t')

        with open("./log/storage/%s.json"%tx_hash,"w",encoding="utf-8") as f:
            f.write(str(evm.Storage))

    return evm.Storage, {"read":evm.readStorage,"write":evm.writeStorage}

def load_group(data_file="./data/game_group.csv") -> 'Dict':
    exec_txs = pd.read_csv(data_file,sep=',')
    group = {}
    for row, exec_tx in exec_txs.iterrows():
        if exec_tx['data'] not in group:
            group[exec_tx['data']] = [exec_tx['transaction_hash']]
        else:
            group[exec_tx['data']].append(exec_tx['transaction_hash'])
    
    return group

def load_data(data_file="./data/game_txs.csv") -> 'Transaction':
    exec_txs = pd.read_csv(data_file,sep=',').sort_values(by=['block_timestamp','transaction_index'],ascending=(True,True))
    for row, exec_tx in exec_txs.iterrows():
        if exec_tx['receipt_status'] == 0: # ignore failed transactions
            continue
        print("\r%d"%row,end='')
        yield Transaction(
            tx_hash=exec_tx['hash'],
            msg_caller=exec_tx['from_address'],
            msg_to=exec_tx['to_address'] if type(exec_tx['to_address']) != type(1.0) else '0', # create tx has no to_address
            msg_value=int(exec_tx['value']),
            msg_input=exec_tx['input'],
            timestamp=exec_tx['block_timestamp']
        )

def mk_dirs():
    if not os.path.exists("./log/storage"):
        os.makedirs("./log/storage")
    
    if not os.path.exists("./log/storage_readwrite"):
        os.makedirs("./log/storage_readwrite")
    
    if not os.path.exists("./log/running"):
        os.makedirs("./log/running")

def replay_transactions(tx_file:str="./data/game_txs.csv"):
    storage_modified = {}
    for tx_idx, tx in enumerate(load_data(tx_file)):
        if tx_idx == 0:
            opcodes,storage = execute_init(tx)
            continue
        if tx.get("tx_hash") == "0x8b20e7edcdb9a58a9d7b5fe08795ba0ff11bb8b4e0e1ebffeba03e2e50075681":
            verbose = True
        else:
            verbose = False
        storage, storage_read_write = execute_tx(
            storage=storage,
            transaction=tx,
            opcodes=opcodes,
            verbose=verbose
        )
        storage_modified[tx.get("tx_hash")] = storage_read_write
       
    with open("result.json","w",encoding="utf-8") as f:
        json.dump(storage_modified,f,indent='\t')

if __name__ == "__main__":
    mk_dirs()
    replay_transactions(tx_file="./data/bounty_txs.csv")

    print()