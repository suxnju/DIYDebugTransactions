import sha3

def keccak256(plain:str) -> str:
    plain = plain.encode("gbk")
    k = sha3.keccak_256()
    k.update(plain)
    return k.hexdigest()