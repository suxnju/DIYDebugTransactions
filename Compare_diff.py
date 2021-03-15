from Structure.utils import storage_diff
import json

with open("./data/storage/0x0f740f087df67006f6762169d93aa97798ab51493c673d7c15a5e9aa549f238f.json","r") as f:
    s1 = json.load(f)

with open("./storage_01.json","r") as f:
    s2 = json.load(f)

storage_diff(s1,s2)
