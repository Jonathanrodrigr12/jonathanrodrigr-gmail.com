import pymongo
import json


class MongoDBContext():

    @staticmethod
    def connect():
        try:
            MONGODB_HOST = 'mongodbc'
            MONGODB_PORT = '27017'
            MONGODB_TIMEOUT = 1000
            MONGODB_DATABASE = 'TESTDB'
            data = {}
            URI_CONNECTION = "mongodb://root:example@" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"
            return pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT, maxPoolSize=10) 
        except Exception as Error:
            print(Error)
