__author__ = "Giovanni \"Talorno\" Ricciardi <talorno@mate-desktop.org>"


import feedparser
import datetime
import time
import dateutil
import re
import dateParser


class pack:
	name = "xxx"
	filename = "xxx"
	version = "0.0.0"
	date_published = "0"

	def popola(self,name,filename,version,date_pub):
		self.name=name
		self.filename=filename
		self.version=version
		self.date_pub=date_pub

	def getName(self):
		print self.name


# test
#now = datetime.datetime.now()
#localtime = time.localtime(time.time())

now = time.strftime("%Y-%m-%d %H:%M:%S")

now = now.replace('|/|', '')

#Scrittura della data di esecuzione nel file temporaneo
out_file = open("last.db.temp","w")
out_file.write(str(now)+"|\|\n")
out_file.close()

# Lettura dell'ultima data di controllo dal file db
in_file = open("last.db","r")
timecheck = in_file.read()
last_check = timecheck.replace('|-|', '')
last_check = dateParser.parseDateTime(last_check)

in_file.close()




python_wiki_rss_url = "http://pub.mate-desktop.org/rss.xml"

feed = feedparser.parse( python_wiki_rss_url )

feed[ "items" ]

entries = []
entries.extend( feed[ "items" ] )


toCompile = []


# createPackage si occupa di ricavare le informazioni necessarie dall'elemento del feed,creare
# un oggetto di tipo package e ritornarlo
def createPackage(entry):

	t = entry.title[-12:-7]

	version = t
	name = entry.title[:-13]
	name = name.title()
	name = name.replace('-',' ')

	

	p=pack();
 
	p.popola(name,entry.title,version,entry.published_parsed)

	
	# print "--start--"

	# print p.name
	# print p.filename
	# print p.version
	# print p.date_pub
	# print "--end --"


	return p


# accodo in toCompile tutti i pacchetti piu' recenti dell'ultima data di controllo
# attualmente uso localtime per comodita' ma ovviamente bisognera'
# salvare la data dell'ultimo controllo



# for i in entries:


# 	if i["published_parsed"] < last_check:
# 		t = createPackage(i)
# 		toCompile.append(t)


		

#for p in toCompile:
	# print "--start--"
	# print p.name
	# print p.filename
	# print p.version
	# print p.date_pub
	# print "--end--"


