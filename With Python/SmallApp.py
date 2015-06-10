import bottle
import pymongo
from pymongo import MongoClient

@bottle.route('/')
def index():
	#connection to DB
	connection=MongoClient('localhost',27017)

	#db
	db=connection.test;

	names=db.names;

	item=names.find_one();

	return '<b>Hello %s|</b>' % item['name']

bottle.run(host = 'localhost',port = 8090)