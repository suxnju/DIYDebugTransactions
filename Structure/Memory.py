from typing import Dict

import json
class EVM_memory:
	def __init__(self,memory:Dict):
		self.memory = memory
	
	def __str__(self):
		# return ",".join([
		# 	hex(self.memory[i]) for i in range(10) if i in self.memory.keys()
		# 	]
		# )
		return json.dumps(
			{
				hex(key):hex(self.memory[key]) for key in self.memory.keys()},
			indent='\t'
		)

	def set_value(self,offset:int,value:int):
		assert offset % 32 == 0

		self.memory[offset//32] = value

	# def get(self,offset:int,length) -> int:
	# 	assert offset % 32 == 0

	# 	return self.memory[offset//32]

	def get(self,offset:int,length:int=1) -> str:
		assert offset % 32 == 0
		
		result = ""
		for i in range(offset//32,offset//32+length):
			result += hex(self.memory[i]).lstrip("0x").rjust(64,"0")
		
		return result