from sample import Media

media = Media()
addFile = "wanEnv-env/file_example_WAV_1MG.wav"

def wav_file():
   dataReturn = media.read_file(addFile)
   dataHex = media.read_hex(data=dataReturn)
   print(dataHex[0:30])
   dataByte = dataHex[10:14]
   dec = int(dataByte, 16)
   print(f"Chunksize = {dec}")

wav_file()