"""

"""


import binascii

hexRange = 100
dataStart = 10
dataEnd = 24
addFile = "wanEnv-env/file_example_WAV_1MG.wav"

class Media:

    def format_data(self, *args):
        aList = list(*args)
        con = []
        n = 0 
        # Itterate through collecting databytes in nested list by given data range and reverse data.  
        for i in range(0, (int(len(aList)/2))):
            i = aList[n:(n+2)]
            con.append(i)
            n += 2
        con.reverse()

        n = 0
        # Covert databytes to readable format from list(HEX) to interger to get value (bit) 
        for i in range(len(con)):
            try:
                if n is 0:
                    fin2 = con[0] + con[1]
                    n += 2
                if n >= 2:
                    fin = fin2 + con[n]
                    n += 1 
            except IndexError:
                pass
        print(type(fin))
        st = ""     
        for f in fin:
            st += f
            
        value = int(st, 16)
        return value

    def read_file(self, *args):
        with open(*args,"rb") as f:
            data = f.read()
            dataHex = self.read_hex(data)
            dataByte = dataHex[0:hexRange]
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

    def read_hex(self, *args):
        dataHex = binascii.hexlify(*args)
        return dataHex
    # Decode data file in readable Hex format.
    def decode_hex(self, dataStr, dataStart, dataEnd):
        fileExt = bytearray.fromhex(dataStr[dataStart:dataEnd]).decode("ISO-8859-1")
        return fileExt


if __name__ == "__main__":
    media = Media()
    media.read_file(addFile)
    
    


