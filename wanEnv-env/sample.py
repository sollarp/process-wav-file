import binascii


with open("wanEnv-env/file_example_WAV_1MG.wav","rb") as f:
    data = f.read()
    dataHex = binascii.hexlify(data)
    listByte = dataHex[0:300]
    listStr = listByte.decode()
    g = bytearray.fromhex(listStr).decode("ISO-8859-1")
    print(g)





