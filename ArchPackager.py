import feedparser
import datetime
import time
import re


class package:
	name = "xxx"
	filename = "xxx"
	version = "0.0.0"
	date_published = "0"

	def populate(self,name,filename,version,date_pub):
		self.name=name
		self.filename=filename
		self.version=version
		self.date_pub=date_pub

	def getName(self):
		return self.name


now = datetime.datetime.now()
localtime = time.localtime(time.time())

python_wiki_rss_url = "http://pub.mate-desktop.org/rss.xml"

feed = feedparser.parse( python_wiki_rss_url )

feed[ "items" ]

entries = []
entries.extend( feed[ "items" ] )


toCompile = [[package]]


# createPackage si occupa di ricavare le informazioni necessarie dall'elemento del feed,creare
# un oggetto di tipo package e ritornarlo
def createPackage(entry):

	# converted=nomeFile.strip(suffix)
	name = entry.title[:-13]
	name = name.title()
	name = name.replace('-',' ')

	version = entry.title[13:]

	p=package()

	p.populate(p,name,entry.title,entry.published_parsed)
	
	return p


# accodo in toCompile tutti i pacchetti piu' recenti dell'ultima data di controllo
# attualmente uso localtime per comodita' ma ovviamente bisognera'
# salvare la data dell'ultimo controllo

for i in entries:
	if i["published_parsed"] < localtime:
		toCompile.append(createPackage(i))
		# createPackage(i)
		

for p in toCompile:
	print p

