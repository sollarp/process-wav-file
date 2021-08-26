import binascii


hexRange = 100
dataRange = 24

def read_file():
    with open("wanEnv-env/file_example_AVI_1920_2_3MG.avi","rb") as f:
        data = f.read()
        dataHex = read_hex(data)
        dataByte = dataHex[0:hexRange]
        #print(dataStr[19:32])
        dataStr = bytes_to_str(dataByte)
        fileExt = decode_file(dataStr)
        if "WAVE" in fileExt:
            print(fileExt)
        elif "AVI" in fileExt:
            print('This file avi')
        #proba(dataStr)


def bytes_to_str(dataByte):
    dataStr = dataByte.decode()
    return dataStr

def read_hex(data):
    dataHex = binascii.hexlify(data)
    return dataHex



def decode_file(dataStr):
    fileExt = bytearray.fromhex(dataStr[10:dataRange]).decode("ISO-8859-1")
    return fileExt


if __name__ == "__main__":
    read_file()
    


