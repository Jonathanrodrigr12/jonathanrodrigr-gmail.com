import json 
import time
from app.utils.region_utils import RegionAll
from app.utils.encrypt_utils import Encryption
from app.utils.create_table import TablePandaUtils
from app.infrastructure.context.sqlite\
     import SqlLiteContext
from app.infrastructure.context.mongo\
     import MongoDBContext     


class RegionAllService():
    @staticmethod 
    def create_region():
        try:
            data = []
            """ Create region table"""
            region = RegionAll()
            connection = SqlLiteContext().connect()
            tableCreate = TablePandaUtils()
            encrypt = Encryption()
            response = region.get_region_all()
            responseArray = json.loads(response.text)
            for value in responseArray:
                start_time = time.time()
                data.append([
                    value['region'],
                    value['name'],
                    encrypt.encrypt_value(value['languages']),
                    (time.time() - start_time)
                ])
            
            tableCreate.create_table(data,['Region','City Name','Languaje','time'], connection)
            RegionAllService.import_data_mongo()
        except Exception as Error:

            print(Error)

        finally:
            connection.close()

    @staticmethod 
    def import_data_mongo():
        MONGODB_DATABASE = 'DBREGION'
        client = MongoDBContext().connect()
        db = client[MONGODB_DATABASE]['REGION']
        with open('./data/data.json') as f:
            data = [json.loads(values) for values in f]
            db.insert_many(data)
        client.close()               