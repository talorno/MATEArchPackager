import feedparser
import datetime
import time

now = datetime.datetime.now()
localtime = time.localtime(time.time())

python_wiki_rss_url = "http://pub.mate-desktop.org/rss.xml"

feed = feedparser.parse( python_wiki_rss_url )

feed[ "items" ]

entries = []
entries.extend( feed[ "items" ] )

toCompile = []


# print entries[3]["title"], entries[3]["published_parsed"][0:15]


# print now
# print localtime
# print localtime[0:15]

# enqueue aggiunge un pacchetto alla coda di compilazione
def enqueue(nomepacchetto,nomefile):
	#blabla
	print nomepacchetto,nomefile
	return 1 


# nameConvert ricava il nome del pacchetto dal nome del file
def nameConvert(nomefile):
	#ricava nome pacchetto da file
	#ritorna nome
	return nomefile



for i in entries:
	# print i["title"], i["published_parsed"][0:15]
	if i["published_parsed"] < localtime:
		enqueue(nameConvert(i["title"]),i["title"])



