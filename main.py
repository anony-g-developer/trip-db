#!/usr/bin/python
import sys, re, string, crypt

def mktripcode(pw):
	pw = pw.decode('utf_8', 'ignore').encode('shift_jis', 'ignore').replace('"', '&quot;').replace("'", '').replace('<', '&lt;').replace('>', '&gt;').replace(',', ',')
	salt = (pw + '...')[1:3]
	salt = re.compile('[^\.-z]').sub('.', salt)
	salt = salt.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
	trip = crypt.crypt(pw, salt)[-10:]
	return trip

while True:
	if re.search(sys.argv[1],string.lower(mktripcode(str(x))))>-1:
		print x, ":", mktripcode(str(x))
	elif x % 100000 == 0:
		print x
	x += 1
