import random
import string
def CodeFunc():
    codeStr = input("Write message: ")
    if(len(codeStr) < 3):
        return codeStr[::-1]

    resStr = codeStr[1: ]
    firStr = codeStr[0]
    firstLet = GenRan()
    lastLet = GenRan()
    return f"{firstLet + resStr + firStr + lastLet}"

def GenRan():
    res = ''.join((random.choice(string.ascii_lowercase) for x in range(3)))
    return res

def DecodeFunc():
    decodeStr = input("Write Sniffer: ")
    if(len(decodeStr) < 3):
        return decodeStr[::-1]
    firStr = decodeStr[3: ]
    resStr = firStr[:-3]
    remainLett = resStr[: -1]
    firstLett = resStr[-1]
    return f"{firstLett + remainLett}"


CodeDecode = input("Do you want to code or decode (code: 'c', decode: 'd'): ")
if(CodeDecode == "c"):
    resultStr = CodeFunc()
    print(resultStr)
elif(CodeDecode == 'd'):
    resultStr = DecodeFunc()
    print(resultStr)
else:
    raise ValueError("Value should be ('c' or 'd')")
