
with open("wanEnv-env/file_example_WAV_1MG.wav","rb") as f:
    data = f.read()
    n = 0
    list = []
    for i in range(len(data)):
        dataHex = hex(data[n])[2:]
        list.append(dataHex)
        n += 1            
    #print(list[0:70])

    listToStr = ''.join(map(str, list))
    print(listToStr[0:70])

    g = bytes.fromhex(dataHex).decode('utf-8')
    print(g)





