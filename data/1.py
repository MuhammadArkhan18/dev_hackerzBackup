import os, sqlite3
from os import listdir
import xml.etree.ElementTree as ET

data_iplist = {}
host = []
value = ''
db = sqlite3.connect("db/iplist.db")
ipl = db.cursor()

def main_process():
	tree = ET.parse('xml_data/net.okitoo.hackers_preferences.xml')
	root = tree.getroot()
	data_ip = ipl.execute("SELECT * FROM IPLIST;")
	dat_ipa = {}

	for ipli in data_ip:
		id_hackerz = str(ipli[0])
		usernamea  = str(ipli[1])
		ip_addressa= str(ipli[2])

		data_data = { usernamea : [ip_addressa, id_hackerz]}
		dat_ipa.update(data_data)

	for child in root:
		if child.tag == "string":
			if child.attrib["name"] == "ip_history":
				data = eval(child.text)
				data_iplist.update(data)

	host = list(data_iplist.keys())

	for i in range(0, len(host)-1):
		username  = data_iplist[host[i]]['title']
		ip_address= data_iplist[host[i]]['ip']
		tut = 0

		if username in dat_ipa:
			if ip_address == dat_ipa[username][0]:
				tut = True
			elif ip_address != dat_ipa[username][0]:
				tut = False

		if tut == 0:
			ipl.execute("INSERT INTO IPLIST(USERNAME, IP_ADDRESS) VALUES( '{}', '{}');".format(username[:-10], ip_address))

		elif tut == True:
			pass

		elif tut == False:
			ipl.execute("UPDATE IPLIST SET IP_ADDRESS= '{}' WHERE ID= {};".format(ip_address, dat_ipa[username][1]))

	db.commit()
	db.close()

	print("Success Backup!")

try:
	main_process()

except Exception as e:
	msg = "Please root your device!\n"
	problem = "Problem: "+str(e)

	if str(e) == "no such table: IPLIST":
		ipl.execute("CREATE TABLE 'IPLIST' ('ID' INTEGER, 'USERNAME' TEXT, 'IP_ADDRESS' TEXT, PRIMARY KEY('ID'));")
		db.commit()
		main_process

	elif str(e) != "no such table: IPLIST":
		print(msg+problem)

finally:
	db.close()
