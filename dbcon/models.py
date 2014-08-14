from django.db import models

from mongoengine import *

class Tweets(EmbeddedDocument):
	date_references = StringField()
	entities = StringField()
	user = StringField()
	id = StringField()
	text = StringField() 
	date = DateTimeField()


class Events(Document):
	meta = {'collection' : 'lecl'}
	keyterms = ListField()
	tweets = ListField(EmbeddedDocumentField(Tweets))
	date = DateTimeField()
	score = FloatField()
	def datestr(self):
		ds = self.date.strftime("%d %B 20%y %A")#to string format
		return ds
	def keylist(self):
		keylist = []
		for k in self.keyterms:
			kt = k[0].title() #capitalization
			keylist.append(kt)
		return keylist

