
from googletrans import Translator
import sys,os
#from bitarray import bitarray

def remove_char(str, n):
      first = str[:n] 
      last = str[n+2:]
      return first+last

translator= Translator()
#hindi='नमस्ते'
hindi='ϵϵ'
chk=str(hindi.encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
print(chk)
u=(hindi.encode('utf-8')).hex()
print(u)
print(hindi.encode('utf-8'))
binary=bin(int(u,16))[2:]
print(binary)
print(binary[0])
if (binary[0] and binary[1] and binary[2])=='1':
      print(len(u))
      for i in range(0,len(u),6):
          code=u[i]+u[i+1]+u[i+2]+u[i+3]+u[i+4]+u[i+5]
          print(code)
          dec=bin(int(code,16))[2:]
          print("original",dec)
          out=dec[3:]
          out1=remove_char(out,5)
          out2=remove_char(out1,11)
          print("After removed initial bits",out2)
          print("output", hex(int(out2,2)))
          print('-'*50)
elif ((binary[0] and binary[1])=='1') and (binary[2]=='0'):
      print("ONly 2 bytes")
      for i in range(0,len(u),4):
          code=u[i]+u[i+1]+u[i+2]+u[i+3]
          dec=bin(int(code,16))[2:]
          print("original",dec)
          out=dec[3:]
          out1=remove_char(out,5)
          print("After removed initial bits",out1)
          print("output", hex(int(out1,2)))
          print('-'*50)
