from web3 import Web3
import subprocess
import os

# Get hex from etherscan API
import time
from etherscan.contracts import Contract as api

KEY = "YUZUJHDUH4DQHZJZUHINK1RVXYQ6AMED1R"

def keccak256(plain:str,is_hex:bool=False) -> str:
    if is_hex:
        return Web3.toHex(Web3.keccak(hexstr=plain)).lstrip("0x").rjust(64,"0")
    else:
        return Web3.toHex(Web3.keccak(text=plain)).lstrip("0x").rjust(64,"0")

def storage_diff(groundtruth_storage,generate_storage):
    re_storage = {}
    for key in groundtruth_storage.keys():
        re_storage[int(groundtruth_storage[key]["key"],16)] = int(groundtruth_storage[key]["value"],16)

    re_generage = {}
    for key in generate_storage.keys():
        re_generage[int(key,16)] = int(generate_storage[key],16)

    for key in re_storage.keys():
        if key in re_generage.keys():
            if re_storage[key] == re_generage[key]:
                continue
            else:
                print("%s:\n\tgenerate:%s\n\tgroundth:%s\n"%(hex(key),hex(re_generage[key]),hex(re_storage[key])))
        else:
            print("Lack key:%s"%hex(key))

def hex_fill(value:int,fill_up:int=64,fill_value:str="0") -> str:
    value = hex(value)[2:]
    return "0x" + value.rjust(fill_up,fill_value)

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
    os.remove(file_path)
    return opcodes

# ref: https://github.com/usyd-blockchain/vandal
def disassemble(code_hex:'hex') -> 'opcodes':
    with open("tmp.hex","w",encoding="utf-8") as f:
        f.write(code_hex)
    command = "python D:/0A-COSEC/A-Codes/0A-EthereumProjects/vandal/bin/disassemble {} > {}".format("tmp.hex","tmp.disassemble")
    process = subprocess.Popen(command,shell=True)
    process.wait()
    os.remove("tmp.hex")
    return load_opcodes("tmp.disassemble")


def get_info(address:str):
    left_times = 4
    while left_times:
        left_times -= 1
        try:
            contract_info = api(address=address,api_key=KEY).get_sourcecode()
            return contract_info
        except Exception as e:
            time.sleep(0.4)
    return None

# ref:https://contract-library.com/
def query_address_hex(address:str) -> int:
    address = "0x" + address[2:].rjust(40,"0")
    response = get_info(address)

    return len(response['bytecode'])

if __name__ == "__main__":
    # to_hash = "00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000008"
    # print(keccak256(to_hash,is_hex=True))

    hex_len = query_address_hex("0x056017c55ae7ae32d12aef7c679df83a85ca75ff")
    print(hex_len)
