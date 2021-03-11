from Structure.EVM import EVM,EVM_stack,EVM_memory,EVM_storage

import logging
logging.basicConfig(filename="./LOG.log",level=logging.INFO,filemode='a')

def load_opcodes(file_path):
    opcodes = []
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            opcode = line[1]
            if len(line) > 2:
                args = int(line[-1],16)
            else:
                args = None
            opcodes.append((line[0],opcode,args))
    return opcodes

def load_init():
    """After Constructor Function"""
    stack = [0,0,0,int('0xd579d4fe1e90a03d545e3d8c01dfc19c2ae3b26ad26ba994a1dec89a435a3dc0',16),int('0x2b8',16),int("0xfe1f6a0b",16)]
    memory = {
        0:0,
        1:0,
        2:int('0x80',16),
    }
    storage = {
        0:int("0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",16),#ceoAddress
        1:int("0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",16),#cfoAddress
        2:int("0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",16),#cooAddress
        # 3:0,#newContractAddress
        # 4:0,#tip_total
        5:10000000000000000,#tip_rate
        # 6:0,#paused
        # 7:0,#payoff mapping
        # 8:0,#games
        # 9:0,#gamesidsOf
        # 10:0,#maxgame
        11:30*60,#expireTime
    }

    return stack,memory,storage

def before_init():
    stack = []
    memory = {}
    storage = {}

    return stack,memory,storage

def after_init():
    stack = []
    memory = {}
    storage_tmp = {
        "0x4": "0x0",
        "0x5": "0x2386f26fc10000",
        "0x6": "0x0",
        "0xa": "0x0",
        "0xb": "0x708",
        "0x741542cd8f25b57b0b9e5febe61424a199c8c746cf747b73eb056bc3b15988ed": "0x65",
        "0x16bba9bde6f0081d94a597097dd9e65d92426023fc5565fa84e934adb6329e27": "0x66",
        "0x51b6982d5c48debb5d4f481380063fbc6904d233d7e6d3c2b8b61672f2e27e4": "0xc9",
        "0x6c5942e15257ab7bcb9b9bb9041c45e824b8ce79cae7f957e673c043fd8f4555": "0xc9",
        "0x89764e4724d5b6f4734cb02002996ced9d361f11c01885debd2e3fe0d5f15701": "0x65",
        "0xca01adecc13b9a42e1d19659887bb0849449ccc981bcb32fe401ce46b14eb561": "0x66",
        "0x6c66d2e35b020654ccc237b963f3925205938faf02503e3c1bfc2f7a3d016e21": "0x66",
        "0xe706459878f093bcbf29548d02cefe7e071999b4eaf0f397e129f84becdf51d5": "0xc9",
        "0xff72f25d2d44c50b8c338604e50a89c49f49b37e2ae539bd2993d8cac84c8f21": "0x65",
        "0xc65916d663d52b0a18b63681e34ad6e3e8bb58d57f662b8e7e045ab09fab0385": "0x65",
        "0xb7d6e7eda72a6499ac6f7463fe4432d1d4d344daf6aba19537000f7bc79f0162": "0xc9",
        "0xfdc33378a97f40f6da99911196e5660604897295d22000ba672dd761fbecdbd7": "0xc9",
        "0xc1dcbaa2e1e0d7759851e0c47ec29192c90c8b10a1c82fb2795ced2510d574e5": "0xc9",
        "0x75f3781c7159604cc37f3697b87982e2a06a22f37a9b56d2e5bed5529088cd21": "0x66",
        "0x6908885217db18c3abdd446136634c92ef886652dc29cae881cb7b0346f30fa8": "0x66",
        "0xaeca9595c25d880c9de7027d33645b60a917e45f30ff05c2e90a90f2fa1c2a28": "0x66",
        "0x0": "0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",
        "0x2": "0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",
        "0x1": "0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba"
    }
    storage = {}
    for key,value in storage_tmp.items():
        storage[int(key,16)] = int(value,16)

    return stack,memory,storage

def execute_init():
    opcodes = load_opcodes("./data/init.disassemble")
    evm = EVM(
        Stack=EVM_stack([]),
        Memory=EVM_memory({}),
        Storage=EVM_storage({})
    )
    for i in range(len(opcodes)):
        opcode = opcodes[i]
        if int(opcode[0],16) != evm.pc:
            continue
        if i == len(opcodes) - 1:
            break
        evm.pc = int(opcodes[i+1][0],16)

        evm.args = opcode[2]
        eval_function = "evm.%s()"%opcode[1]
        
        eval(eval_function)

    return evm.Storage

if __name__ == "__main__":
    storage = execute_init()
    evm = EVM(
        Stack=EVM_stack([]),
        Memory=EVM_memory({}),
        Storage=storage
    )
    f = open("runing_log.py","w",encoding="utf-8")
    opcodes = load_opcodes("./data/game.disassemble")
    DEBUG_Point = 0x33
    for i in range(len(opcodes)):
        opcode = opcodes[i]
        if int(opcode[0],16) != evm.pc:
            continue
        if i == len(opcodes) - 1:
            break
        evm.pc = int(opcodes[i+1][0],16)
        if int(opcode[0],16) == DEBUG_Point:
            print()
        f.write("stack:[%s]\nmemory:%s\nstorage:%s\n%s\n\n"%(str(evm.Stack),str(evm.Memory),str(evm.Storage),"="*10+str(opcode)+"="*10))
        f.flush()
        evm.args = opcode[2]
        eval_function = "evm.%s()"%opcode[1]
        
        eval(eval_function)

    f.close()