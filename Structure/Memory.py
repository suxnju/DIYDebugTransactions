from typing import Dict

import json
from .utils import hex_fill

class EVM_memory:
	def __init__(self,memory:str="0"*int("0x60",16)):
		self.memory = memory

	def __str__(self):
		return json.dumps(
			{
				hex(i//2):self.memory[i:i+32] for i in range(0,len(self.memory),32) 
				},
			indent='\t'
		)

	def set_value(self,offset:int,value:int,length:int=32):
		offset = offset * 2
		length = length * 2
		tmp = self.memory
		# fill up zero (right padding)
		if len(tmp) < offset + length:
			tmp = tmp.ljust(offset+length,"0")
		
		tmp = tmp[:offset] + hex(value)[2:].rjust(length,"0") + tmp[offset+length:]
		self.memory = tmp

	def get(self,offset:int,length:int=1) -> str:
		offset = offset *2
		length = length *2
		tmp = self.memory
		# fill up zero (right padding)
		if len(tmp) < offset+length:
			tmp = tmp.ljust(offset+length,"0")
		self.memory = tmp
		return self.memory[offset:offset+length]

if __name__ == "__main__":
	memory_ = EVM_memory()
	memory_.set_value(int('0x80',16),int("5dc12131e65b8f395ab11a2c4e6af717e1b179ba1e3e0db1bcb49b1666382383",16))
	print(str(memory_))
	print(memory_.get(int("0x82",16)))
