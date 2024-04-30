import os
import hashlib
import base64

f =  open('/usr/share/john/password.lst','r') #le o arquivo password.lst
#f = open('/usr/share/wordlists/rockyou_utf8.txt','r')

palavras = f.readlines()

#para cada palavra da lista, o script irá converter para md5, encodar em base64 e depois em sha1, por fim
#irá comparar com a hash fornecida na linha 27

for palavra in palavras:

   #nessa linha é transformado em md5
   md5 = hashlib.md5(palavra.rstrip('\n').encode('utf-8')).hexdigest()

   #nessa linha é transformado em base64
   b64 = base64.b64encode(md5.encode())

   #nessa linha transforma em sha1
   hash = hashlib.sha1(b64).hexdigest()

   #nessa linha compara a hash gerada com a hash informada entre aspas
   if hash == 'INFORMAR_HASH_AQUI':
       print('A senha utilizada é:', palavra.rstrip('\n'))
       break
