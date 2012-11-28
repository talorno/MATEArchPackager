import feedparser
import datetime
import time
import re

now = datetime.datetime.now()
localtime = time.localtime(time.time())

python_wiki_rss_url = "http://pub.mate-desktop.org/rss.xml"

feed = feedparser.parse( python_wiki_rss_url )

feed[ "items" ]

entries = []
entries.extend( feed[ "items" ] )

toCompile = []


# suffix = "-1.5.0.tar.xz"



# enqueue aggiunge un pacchetto alla coda di compilazione
def enqueue(nomepacchetto,nomefile):
	#blabla
	# print nomepacchetto,nomefile
	return 1 


# nameConvert ricava il nome del pacchetto dal nome del file
def nameConvert(nomeFile):

	# converted=nomeFile.strip(suffix)
	converted = nomeFile[:-13]
	converted = converted.title()
	converted = converted.replace('-',' ')
	print converted
	#ritorna nome
	return converted


for i in entries:
	# print i["title"], i["published_parsed"][0:15]
	if i["published_parsed"] < localtime:
		enqueue(nameConvert(i["title"]),i["title"])




