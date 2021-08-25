import binascii


def readfile():
    with open("wanEnv-env/file_example_AVI_1920_2_3MG.avi","rb") as f:
        data = f.read()
        dataHex = binascii.hexlify(data)
        dataByte = dataHex[0:100]
        dataStr = dataByte.decode()
        #print(dataStr[19:32])
        fileExt = bytearray.fromhex(dataStr[10:24]).decode("ISO-8859-1")
        if "WAVE" in fileExt:
            print(fileExt)
        elif "AVI" in fileExt:
            print('This file avi')
        #proba(dataStr)

def proba(dataStr):
    print(dataStr)


if __name__ == "__main__":
    readfile()
    


