from sample import Media


media = Media()
addFile = "wanEnv-env/Ensoniq-ZR-76-01-Dope-77.wav"
dataReturn = media.read_file(addFile)
dataHex = media.read_hex(dataReturn)

def handler(a, b):
   dataByte = dataHex[a:b]
   data = media.bytes_to_str(dataByte)
   value = media.format_data(data)
   return value
   
def chunk_size():
   a = 10
   b = 16
   getData = handler(a, b)
   print(f"Chunksize = {getData}")

def subchunk_one_size():
   a = 32
   b = 40
   getData = handler(a, b)
   print(f"Subchunk size = {getData}")

def audio_format():
   a = 40
   b = 44
   getData = handler(a, b)
   print(f"Audio format = {getData}")

def chanel_number():
   a = 44
   b = 48
   getData = handler(a, b)
   print(f"Audio format = {getData}")

      

#chunk_size()
chanel_number()