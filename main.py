#!/usr/bin/python
import sys, re, string, crypt, random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def mktripcode(pw):
	pw = pw.decode('utf_8', 'ignore').encode('shift_jis', 'ignore').replace('"', '&quot;').replace("'", '').replace('<', '&lt;').replace('>', '&gt;').replace(',', ',')
	salt = (pw + '...')[1:3]
	salt = re.compile('[^\.-z]').sub('.', salt)
	salt = salt.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
	trip = crypt.crypt(pw, salt)[-10:]
	return trip

while True:
	x = ''.join(random.choice(chars) for n in xrange(8))
	print x, ":", mktripcode(str(x))
