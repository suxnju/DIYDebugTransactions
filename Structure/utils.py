from web3 import Web3
import subprocess
import os

# Get hex from contract-lib
import requests
import json
import time
url_headers = {
	"User-Agent":"Mozilla/5.0 (Linux; Android 9.0; Z832 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
	"Connection":"close"
}
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


def Get_url(url):
	left_try = 4
	while left_try:
		try:
			response = requests.get(url, headers=url_headers)
			return response.json()
		except Exception as e:
			time.sleep(0.5)
			left_try -= 1
			continue
	return ''

# ref:https://contract-library.com/
def online_query_address_hex(address:str) -> int:
    address = "0x" + address[2:].rjust(40,"0")
    url = "https://contract-library.com/api/contracts/Ethereum/" + address 
    response = Get_url(url)

    return len(response['bytecode'])

def online_query_address(address:str) -> 'Dict':
    from etherscan.contracts import Contract as api
    KEY = "YUZUJHDUH4DQHZJZUHINK1RVXYQ6AMED1R"
    left_times = 4
    while left_times:
        left_times -= 1
        try:
            contract_info = api(address=address,api_key=KEY).get_sourcecode()
            return contract_info
        except Exception as e:
            time.sleep(0.4)
    logging.error("error in address %s"%address)
    return None

if __name__ == "__main__":
    # to_hash = "00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000008"
    # print(keccak256(to_hash,is_hex=True))

    # hex_len = online_query_address_hex("0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359")
    # print(hex_len)

    address_info = online_query_address("0x8631316985dcbd442db6136fd0fa0e21d9767f8d")

    print()