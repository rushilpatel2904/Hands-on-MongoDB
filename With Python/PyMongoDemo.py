import pymongo;
from pymongo import MongoClient

#Connection to the database
conection = MongoClient('localhost',27017)

db=conection.test

names=db.names

item = names.find_one()

print item['name']