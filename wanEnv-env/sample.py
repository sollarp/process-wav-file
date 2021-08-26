import binascii

hexRange = 100
dataStart = 10
dataEnd = 24
#addFile = "wanEnv-env/file_example_AVI_1920_2_3MG.avi"

class Media:

    def read_file(self, addFile):
        with open(addFile,"rb") as f:
            data = f.read()
            dataHex = self.read_hex(data)
            dataByte = dataHex[0:hexRange]
            #print(dataStr[19:32])
            dataStr = self.bytes_to_str(dataByte)
            fileExt = self.decode_hex(dataStr, dataStart, dataEnd)
            if "WAVE" in fileExt:
                print(fileExt)
            elif "AVI" in fileExt:
                print('This file avi')
        return data


    def bytes_to_str(self, dataByte):
        dataStr = dataByte.decode()
        return dataStr

    def read_hex(self, data):
        dataHex = binascii.hexlify(data)
        return dataHex

    def decode_hex(self, dataStr, dataStart, dataEnd):
        fileExt = bytearray.fromhex(dataStr[dataStart:dataEnd]).decode("ISO-8859-1")
        return fileExt


if __name__ == "__main__":
    media = Media()
    media.read_file(addFile)
    
    


