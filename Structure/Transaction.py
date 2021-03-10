import time
import datetime

def get_timestamp(block_time,UTC=True):
	if UTC:
		dt = datetime.datetime.strptime(block_time, "%Y-%m-%d %H:%M:%S UTC") + datetime.timedelta(hours=8)
	else:
		dt = datetime.datetime.strptime(block_time, "%Y-%m-%d %H:%M:%S")
	timestamp = datetime.datetime.timestamp(dt)
	return int(timestamp)

def get_time(timestamp):
	time_local = time.localtime(timestamp)
	block_time = time.strftime("%Y-%m-%d %H:%M:%S UTC",time_local)
	return block_time

class Transaction:
	From = int("0x5dc12131e65b8f395ab11a2c4e6af717e1b179ba",16)
	To = int("0xa8f9c7ff9f605f401bde6659fd18d9a0d0a802c5",16)
	Value = 50000000000000000
	Input = int("0xfe1f6a0bd579d4fe1e90a03d545e3d8c01dfc19c2ae3b26ad26ba994a1dec89a435a3dc00000000000000000000000000000000000000000000000000000000000000000",16)
	Timestamp = get_timestamp("2018-08-19 15:05:16 UTC")

# if __name__ == "__main__":
# 	print(get_timestamp("2018-08-19 15:05:16 UTC"))
# 	print(get_time(1534691116))