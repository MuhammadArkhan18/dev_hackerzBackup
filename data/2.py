import os, sqlite3
from os import listdir
import xml.etree.ElementTree as ET

file = open('export_ip/iplist.txt', 'a')
qfi  = open('export_ip/iplist.txt', 'r')
msg = ''
q = 1
user = []
ip_a = []
data_file = {}
data_db   = {}
db = sqlite3.connect("db/iplist.db")
ipl= db.cursor()

try:
	data_l = db.execute("SELECT * FROM IPLIST;")

	for i in qfi:
		if i == "" or i == "\n":
			pass

		elif q == 1:
			p = i.replace("Username: ", "")
			w = p.replace("\n", "")

			user += [w]

			q += 1

		elif q == 2:
			p = i.replace("IP Address: ", "")
			w = p.replace("\n", "")
			ip_a+= [w]

			q = 1

	qfi.close()

	for i in  range(0, len(user)-1):
		usern = user[i]
		ipadd = ip_a[i]

		data_file.update({usern: ipadd})

	for i in data_l:
		print(i)
		username = str(i[1])
		ip_address= str(i[2])
		l = False

		if username in data_file:
			if ip_address == data_file[username]:
				l = True

		if l == False:
			msg += "Username: "+str(i[1])+"\n"
			msg += "IP Address: "+str(i[2])+"\n"
			msg += "\n"

	if msg != '':
		file.write(msg)

	print("Exported to Internal Memory: iplist.txt!")

except Exception as e:
	print("Problem: "+str(e))

finally:
	db.close()
	file.close()
