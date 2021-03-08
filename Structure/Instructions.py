### References:
### https://ethervm.io/

import logging
import functools

from typing import List,Dict

from utils import keccak256
from constant import *

def STOP():
    logging.info("halts exectuion of the contract")

def ADD(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2

	c = input_stack[0]+input_stack[1]
	if c>UPPER:
		logging.warning("Integer overflow")
	c = c%UPPER
	output_stack = [c] + input_stack[2:]
	return output_stack

def MUL(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
        
	c = input_stack[0]*input_stack[1]
	if c>UPPER:
		logging.warning("Integer overflow")
	c = c%UPPER
	output_stack = [c] + input_stack[2:]
	return output_stack

def SUB(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = input_stack[0]-input_stack[1]
	c = c%UPPER

	output_stack = [c] + input_stack[2:]

	return output_stack

def DIV(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = input_stack[0]//input_stack[1]

	output_stack = [c] + input_stack[2:]

	return output_stack

def SDIV(input_stack:List[int]) -> List[int]:
	return DIV(input_stack)

def MOD(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = input_stack[0]%input_stack[1]

	output_stack = [c] + input_stack[2:]

	return output_stack

def SMOD(input_stack:List[int]) -> List[int]:
	return MOD(input_stack)

def ADDMOD(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 3

	return MOD(ADD(input_stack))

def MULMOD(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 3

	return MOD(MUL(input_stack))

def EXP(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
        
	c = input_stack[0]**input_stack[1]
	if c>UPPER:
		logging.warning("Integer overflow")
	c = c%UPPER
	output_stack = [c] + input_stack[2:]
	return output_stack

def SIGNEXTEND(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
    
	b = input_stack[0]
	x = input_stack[1]
	if b > 31:
		y = x
	else:
		pos = 8 * (b + 1)
		sign_bit = (1 << pos-1)
		if x & sign_bit:
			y = x | (UPPER - sign_bit)
		else:
			y = x & (sign_bit - 1)
	output_stack = [y] + input_stack[2:]
	return output_stack

def LT(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = 1 if input_stack[0]<input_stack[1] else 0

	output_stack = [c] + input_stack[2:]
	return output_stack

def GT(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = 1 if input_stack[0]>input_stack[1] else 0

	output_stack = [c] + input_stack[2:]
	return output_stack

def SLT(input_stack:List[int]) -> List[int]:
	return LT(input_stack)

def SGT(input_stack:List[int]) -> List[int]:
	return GT(input_stack)

def EQ(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2    
	c = int(input_stack[0]==input_stack[1])

	output_stack = [c] + input_stack[2:]
	return output_stack

def ISZERO(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 1
	c = int(input_stack[0]==0)

	output_stack = [c] + input_stack[1:]
	return output_stack

def AND(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = input_stack[0] & input_stack[1]

	output_stack = [c] + input_stack[2:]
	return output_stack

def OR(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = input_stack[0] | input_stack[1]

	output_stack = [c] + input_stack[2:]
	return output_stack

def XOR(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	c = input_stack[0] ^ input_stack[1]

	output_stack = [c] + input_stack[2:]
	return output_stack

def NOT(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 1

	output_stack = [~input_stack[0]] + input_stack[1:]
	return output_stack

def BYTE(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	i = input_stack[0]
	x = input_stack[1]

	y = (x>>(248-i*8)) & int('0xff',16)
	output_stack = [y] + input_stack[2:]
	return output_stack

def SHL(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	shift = input_stack[0]
	value = input_stack[1]

	y = value << shift
	output_stack = [y] + input_stack[2:]
	return output_stack

def SHR(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	shift = input_stack[0]
	value = input_stack[1]

	y = value >> shift
	output_stack = [y] + input_stack[2:]
	return output_stack

def SAR(input_stack:List[int]) -> List[int]:
	return SHR(input_stack)

def SHA3(input_stack:List[int],input_memory:List[int]) -> List[int]:
	assert len(input_stack) >= 2
	offset = input_stack[0]
	length = input_stack[1]

	assert offset % 32 == 0
	assert length % 32 == 0

	memory_copy = [hex(i).strip('0x').rjust(32,'0') for i in input_memory]
	to_hash = "".join(memory_copy[offset//32:offset//32+length//32])

	y = keccak256(to_hash)

	output_stack = [y] + input_stack[2:]

	return output_stack

def ADDRESS(input_stack:List[int]) -> List[int]:
	output_stack = [address] + input_stack
	return output_stack

def BALANCE(input_stack:List[int]) -> List[int]:
	assert len(input_stack) > 1

	output_stack = [addr_balance] + input_stack[1:]

	return output_stack

def ORIGIN(input_stack:List[int]) -> List[int]:
	output_stack = [tx_origin] + input_stack

	return output_stack

def CALLER(input_stack:List[int]) -> List[int]:
	output_stack = [msg_caller] + input_stack

	return output_stack

def CALLVALUE(input_stack:List[int]) -> List[int]:
	output_stack = [msg_value] + input_stack

	return output_stack

def CALLDATALOAD(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 1
	i = input_stack[0]
	output_stack = [int(msg_data[i:i+32],16)] + input_stack[1:]

	return output_stack

def CALLDATASIZE(input_stack:List[int]) -> List[int]:
	output_stack = [len(msg_data)/2] + input_stack

	return output_stack

def CALLDATACOPY(input_stack:List[int],input_memory:List[int]) -> List[int]:
	raise ValueError("Not implement error!")

def CODESIZE():
	raise ValueError("Not implement error!")

def CODECOPY():
	raise ValueError("Not implement error!")

def GASPRICE():
	raise ValueError("Not implement error!")

def EXTCODESIZE():
	raise ValueError("Not implement error!")

def EXTCODECOPY():
	raise ValueError("Not implement error!")

def RETURNDATASIZE():
	raise ValueError("Not implement error!")

def RETURNDATACOPY():
	raise ValueError("Not implement error!")

def EXTCODEHASH():
	raise ValueError("Not implement error!")

def BLOCKHASH():
	raise ValueError("Not implement error!")

def COINBASE():
	raise ValueError("Not implement error!")

def TIMESTAMP():
	raise ValueError("Not implement error!")

def NUMBER():
	raise ValueError("Not implement error!")

def DIFFICULTY():
	raise ValueError("Not implement error!")

def GASLIMIT():
	raise ValueError("Not implement error!")

def POP():
	raise ValueError("Not implement error!")

def MLOAD(input_stack:List[int],input_memory:List[int]) -> List[int]:
	assert len(input_stack) >= 1

	offset = input_stack[0]
	assert offset%32 == 0
	value = input_memory[offset/32]

	output_stack = [value] + input_stack[1:]

	return output_stack

def MSTORE(input_stack:List[int],input_memory:List[int]) -> List[int]:
	assert len(input_stack) >= 2

	offset = input_stack[0]
	value = input_stack[1]

	output_stack = input_stack[3:]
	output_memory[offset/32] = value
	return output_stack, output_memory

def MSTORE8():
	raise ValueError("Not implement error!")

def SLOAD(input_stack:List[int],input_storage:Dict) -> List[int]:
	assert len(input_stack) >= 1

	value = input_storage[input_stack[0]]

	output_stack = [value] + input_stack[1:]
	return output_stack

def SSTORE(input_stack:List[int],input_storage:Dict) -> List[int]:
	assert len(input_stack) >= 2

	key = input_stack[0]
	value = input_stack[1]
	input_storage[key] = value
	output_stack = input_stack[2:]
	return output_stack,input_storage

def JUMP(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 1

	output_stack = input_stack[1:]
	return output_stack

def JUMPI(input_stack:List[int]) -> List[int]:
	assert len(input_stack) >= 2

	output_stack = input_stack[2:]
	return output_stack
	
def PC():
	raise ValueError("Not implement error!")

def MSIZE():
	raise ValueError("Not implement error!")

def GAS():
	raise ValueError("Not implement error!")

def JUMPDEST():
	pass

def PUSHXXX(input_stack:List[int],value:int) -> List[int]:
	output_stack = [value] + input_stack[1:]
	return output_stack

PUSH1 = functools.partial(PUSHXXX)
PUSH2 = functools.partial(PUSHXXX)
PUSH3 = functools.partial(PUSHXXX)
PUSH4 = functools.partial(PUSHXXX)
PUSH5 = functools.partial(PUSHXXX)
PUSH6 = functools.partial(PUSHXXX)
PUSH7 = functools.partial(PUSHXXX)
PUSH8 = functools.partial(PUSHXXX)
PUSH9 = functools.partial(PUSHXXX)
PUSH10 = functools.partial(PUSHXXX)
PUSH11 = functools.partial(PUSHXXX)
PUSH12 = functools.partial(PUSHXXX)
PUSH13 = functools.partial(PUSHXXX)
PUSH14 = functools.partial(PUSHXXX)
PUSH15 = functools.partial(PUSHXXX)
PUSH16 = functools.partial(PUSHXXX)
PUSH17 = functools.partial(PUSHXXX)
PUSH18 = functools.partial(PUSHXXX)
PUSH19 = functools.partial(PUSHXXX)
PUSH20 = functools.partial(PUSHXXX)
PUSH21 = functools.partial(PUSHXXX)
PUSH22 = functools.partial(PUSHXXX)
PUSH23 = functools.partial(PUSHXXX)
PUSH24 = functools.partial(PUSHXXX)
PUSH25 = functools.partial(PUSHXXX)
PUSH26 = functools.partial(PUSHXXX)
PUSH27 = functools.partial(PUSHXXX)
PUSH28 = functools.partial(PUSHXXX)
PUSH29 = functools.partial(PUSHXXX)
PUSH30 = functools.partial(PUSHXXX)
PUSH31 = functools.partial(PUSHXXX)
PUSH32 = functools.partial(PUSHXXX)

def DUPXXX(input_stack:List[int],idx:int) -> List[int]:
	assert len(input_stack) > idx+1

	output_stack = [input_stack[idx-1]] + input_stack
	return output_stack

DUP1 = functools.partial(DUPXXX,idx=1)
DUP2 = functools.partial(DUPXXX,idx=2)
DUP3 = functools.partial(DUPXXX,idx=3)
DUP4 = functools.partial(DUPXXX,idx=4)
DUP5 = functools.partial(DUPXXX,idx=5)
DUP6 = functools.partial(DUPXXX,idx=6)
DUP7 = functools.partial(DUPXXX,idx=7)
DUP8 = functools.partial(DUPXXX,idx=8)
DUP9 = functools.partial(DUPXXX,idx=9)
DUP10 = functools.partial(DUPXXX,idx=10)
DUP11 = functools.partial(DUPXXX,idx=11)
DUP12 = functools.partial(DUPXXX,idx=12)
DUP13 = functools.partial(DUPXXX,idx=13)
DUP14 = functools.partial(DUPXXX,idx=14)
DUP15 = functools.partial(DUPXXX,idx=15)
DUP16 = functools.partial(DUPXXX,idx=16)


def SWAPXXX(input_stack:List[int],idx:int) -> List[int]:
	assert len(input_stack) >= idx + 1
	a = input_stack[0]
	b = input_stack[idx]

	input_stack[0] = b
	input_stack[idx] = a
	return input_stack

SWAP1 = functools.partial(SWAPXXX, idx=1)
SWAP2 = functools.partial(SWAPXXX, idx=2)
SWAP3 = functools.partial(SWAPXXX, idx=3)
SWAP4 = functools.partial(SWAPXXX, idx=4)
SWAP5 = functools.partial(SWAPXXX, idx=5)
SWAP6 = functools.partial(SWAPXXX, idx=6)
SWAP7 = functools.partial(SWAPXXX, idx=7)
SWAP8 = functools.partial(SWAPXXX, idx=8)
SWAP9 = functools.partial(SWAPXXX, idx=9)
SWAP10 = functools.partial(SWAPXXX, idx=10)
SWAP11 = functools.partial(SWAPXXX, idx=11)
SWAP12 = functools.partial(SWAPXXX, idx=12)
SWAP13 = functools.partial(SWAPXXX, idx=13)
SWAP14 = functools.partial(SWAPXXX, idx=14)
SWAP15 = functools.partial(SWAPXXX, idx=15)
SWAP16 = functools.partial(SWAPXXX, idx=16)

def LOG0():
	raise ValueError("Not implement error!")

def LOG1():
	raise ValueError("Not implement error!")

def LOG2():
	raise ValueError("Not implement error!")

def LOG3():
	raise ValueError("Not implement error!")

def LOG4():
	raise ValueError("Not implement error!")

def PUSH():
	raise ValueError("Not implement error!")

def DUP():
	raise ValueError("Not implement error!")

def SWAP():
	raise ValueError("Not implement error!")

def CREATE():
	raise ValueError("Not implement error!")

def CALL():
	raise ValueError("Not implement error!")

def CALLCODE():
	raise ValueError("Not implement error!")

def RETURN():
	raise ValueError("Not implement error!")

def DELEGATECALL():
	raise ValueError("Not implement error!")

def CREATE2():
	raise ValueError("Not implement error!")

def STATICCALL():
	raise ValueError("Not implement error!")

def REVERT():
	raise ValueError("Not implement error!")

def SELFDESTRUCT():
	raise ValueError("Not implement error!")

if __name__ == "__main__":
	print(ADDMOD([2,3,3]))