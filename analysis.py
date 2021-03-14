from Structure.EVM import EVM,EVM_stack,EVM_memory,EVM_storage

import os
import json
import logging
import pandas as pd

from Structure.Constant import OPCODE_TO_INSTR
from Structure.Transaction import Transaction

def load_opcodes(file_path:str) -> 'Dict':
    opcodes = {}
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            opcode = line[1]
            if len(line) > 2:
                args = int(line[-1],16)
            else:
                args = None
            opcodes[int(line[0],16)] = (opcode,args)
    return opcodes

def execute_init():
    opcodes = load_opcodes("./data/init.disassemble")
    
    tx_0 = Transaction(
        tx_hash="0x79a09f9843b1248b192ea05f36b60686d3ca5bbee7020f7431aed669131516c7",
        msg_caller="0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",
        msg_value=0,
        msg_input="0", # mask input
        timestamp="2018-08-19 14:50:21 UTC"
    )

    evm = EVM(
        Stack=EVM_stack(),
        Memory=EVM_memory(),
        Storage=EVM_storage({}),
        Transaction=tx_0
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

    return evm.Storage, {"read":evm.readStorage,"write":evm.writeStorage}

def execute_tx(storage:'EVM_storage',transaction:'Transaction',opcodes:'Dict',DEBUG_Point:int=0x0):
    evm = EVM(
        Stack=EVM_stack(),
        Memory=EVM_memory(),
        Storage=storage,
        Transaction=transaction
    )
    tx_hash = transaction.get("tx_hash")
    
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

    return evm.Storage, {"read":evm.readStorage,"write":evm.writeStorage}

def load_data(data_file="./data/0xa8f9c7ff9f605f401bde6659fd18d9a0d0a802c5.csv") -> 'Transaction':
    exec_txs = pd.read_csv(data_file,sep=',').sort_values(by=['block_timestamp','nonce','transaction_index'],ascending=(True,True,True))
    for row, exec_tx in exec_txs.iterrows():
        if exec_tx['hash'] == "0x79a09f9843b1248b192ea05f36b60686d3ca5bbee7020f7431aed669131516c7": # init has executed
            continue
        if exec_tx['receipt_status'] == '0': # ignore failed transactions
            continue
        print("\r%d"%row,end='')
        yield Transaction(
            tx_hash=exec_tx['hash'],
            msg_caller=exec_tx['from_address'],
            msg_value=int(exec_tx['value']),
            msg_input=exec_tx['input'],
            timestamp=exec_tx['block_timestamp']
        )

if __name__ == "__main__":
    storage, storage_init = execute_init()
    
    storage_modified = {
        "init":storage_init
    }
    opcodes = load_opcodes("./data/game.disassemble")

    for tx in load_data():
        storage, storage_read_write = execute_tx(
            storage=storage,
            transaction=tx,
            opcodes=opcodes
        )
        storage_modified[tx.get("tx_hash")] = storage_read_write
    
    with open("result.json","w",encoding="utf-8") as f:
        json.dump(storage_modified,f,indent='\t')
    print()