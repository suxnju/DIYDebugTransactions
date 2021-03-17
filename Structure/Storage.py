from typing import Dict
import json
from .utils import hex_fill

class EVM_storage:
	def __init__(self,storage:Dict):
		self.storage = storage

	def __str__(self):
		return json.dumps(
			{
				hex_fill(key):hex_fill(self.storage[key]) for i,key in enumerate(self.storage.keys()) if i < 10
				},
			indent='\t'
		)

	def get(self,key:int) -> int:
		# assert key in self.storage.keys()
		if key in self.storage.keys():
			return self.storage[key]
		else:
			return 0
	
	def set_key(self,key:int,value:int):
		self.storage[key] = value
