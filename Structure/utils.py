from web3 import Web3

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

if __name__ == "__main__":
    to_hash = "00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000008"
    print(keccak256(to_hash,is_hex=True))
