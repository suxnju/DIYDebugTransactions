# import requests
from lxml import etree

# URL = "https://ethervm.io/"

# res = requests.get(URL)
# ethervm = etree.HTML(res.text)
ethervm = etree.parse('C:/Users/Su/Desktop/Ethereum Virtual Machine Opcodes.html',etree.HTMLParser())

trs = ethervm.xpath("/html/body/div[2]/div/table[3]/tbody/tr")

f = open("table.txt","w",encoding="utf-8")

OpcodeList = []

for tr in trs:
    tds = tr.xpath("./td")
    Opcode = tds[0].xpath("string(.)").strip()
    Mnemonic = tds[1].xpath("string(.)").strip()
    Expression = tds[-2].xpath("string(.)").strip().replace("\n","").replace(" ","")
    Notes = tds[-1].xpath("string(.)").strip()
    if Mnemonic != "Invalid":
        f.write('\t"%s":(0x%s,"%s","%s",%s),\n'%(Mnemonic,Opcode,Expression,Notes,Mnemonic))
        OpcodeList.append(Mnemonic)
    # f.flush()

for opcode in OpcodeList:
    f.write("def %s():\n\tpass\n\n"%opcode)

f.close()