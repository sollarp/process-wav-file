"""
Reads Hex data in this case wav and avi file formats and returns the toplevel definition of a files.


The canonical WAVE format starts with the RIFF header:

0         4   ChunkID          Contains the letters "RIFF" in ASCII form
                               (0x52494646 big-endian form).
4         4   ChunkSize        36 + SubChunk2Size, or more precisely:
                               4 + (8 + SubChunk1Size) + (8 + SubChunk2Size)
                               This is the size of the rest of the chunk 
                               following this number.  This is the size of the 
                               entire file in bytes minus 8 bytes for the
                               two fields not included in this count:
                               ChunkID and ChunkSize.
8         4   Format           Contains the letters "WAVE"
                               (0x57415645 big-endian form).

Ect.         ...................................................

For more information https://en.wikipedia.org/wiki/WAV
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
        # Iterate through a nested list of databytes by given data range and reverse data.  
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

    # Looking for file extension type AVI or WAV from Hex data.
    def read_file(self, *args):
        with open(*args,"rb") as f:
            data = f.read()
            dataHex = self.read_hex(data) # Remove "x" from front of bytes.
            dataByte = dataHex[0:hexRange] # Range of bytes
            dataStr = self.bytes_to_str(dataByte) # Integer in string format
            fileExt = self.decode_hex(dataStr, dataStart, dataEnd) # Convert Integer to letters.
            if "WAVE" in fileExt:
                print(f"This file is {fileExt} (wav) format.")
            elif "AVI" in fileExt:
                print('This file avi')
        return data

    # Converts bytes to string.
    def bytes_to_str(self, dataByte):
        dataStr = dataByte.decode()
        return dataStr
   
    # Decode data file in readable Hex format.
    def read_hex(self, *args):
        dataHex = binascii.hexlify(*args)
        return dataHex

     # Translate string to Hex.
    def decode_hex(self, dataStr, dataStart, dataEnd):
        fileExt = bytearray.fromhex(dataStr[dataStart:dataEnd]).decode("ISO-8859-1")
        return fileExt


if __name__ == "__main__":
    media = Media()
    media.read_file(addFile)
    
    


