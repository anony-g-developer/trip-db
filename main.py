#!/usr/bin/python
import sys, re, string, crypt, random, sqlite3

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def mktripcode(pw):
	pw = pw.decode('utf_8', 'ignore').encode('shift_jis', 'ignore').replace('"', '&quot;').replace("'", '').replace('<', '&lt;').replace('>', '&gt;').replace(',', ',')
	salt = (pw + '...')[1:3]
	salt = re.compile('[^\.-z]').sub('.', salt)
	salt = salt.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
	trip = crypt.crypt(pw, salt)[-10:]
	return trip

conn = sqlite3.connect('trips.db')
curr = conn.cursor()
curr.execute('CREATE TABLE IF NOT EXISTS Trips(pass TEXT, trip TEXT);')
conn.commit()

while True:
	x = ''.join(random.choice(chars) for n in xrange(8))
	z = mktripcode(x)
	print x,':',z
	curr.execute('INSERT INTO Trips VALUES(\''+x+'\',\''+z+'\');')
	conn.commit()
