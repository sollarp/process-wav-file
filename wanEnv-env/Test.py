from numpy import byte, int0
from sample import Media


media = Media()
addFile = "wanEnv-env/file_example_WAV_1MG.wav"
dataReturn = media.read_file(addFile)
dataHex = media.read_hex(data=dataReturn)

def handler(a, b):
   dataByte = dataHex[a:b]
   #print(f"data final = {dataByte}")
   d = media.bytes_to_str(dataByte)
   f = list(d)
   con = []
   n = 0 
   for i in range(0, (int(len(f)/2))):
      i = f[n:(n+2)]
      con.append(i)
      n += 2
   con.reverse()

   n = 0
   for i in range(len(con)):
      try:
         if n is 0:
            fin2 = con[0] + con[1]
            n += 2
         if n >= 2:
            #fin.extend(con[n])
            fin = fin2 + con[n]
            n += 1 
      except IndexError:
         pass
      
   n = 0
   st = ""     
   for f in fin:
      st += f

   #for i in range(len(fin)):
   #   try:
   #      if n is 0:
   #         fin3 = fin[0:4]
   #         fin3 = list(fin3)
   #         print(f" elso {fin3}")
   #         n += 3
   #      if n >= 3:
   #         fin3.extend(con[n])
   #         #fin4 = fin3 + fin[n]
   #         n += 1 
   #   except IndexError:
   #      pass
      
   value = int(st, 16)
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

#chunk_size()
subchunk_one_size()