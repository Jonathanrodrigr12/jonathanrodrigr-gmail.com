import psycopg2

class ModelContext():
    def ConnectionPostgreSql(self):
        con=psycopg2.connect(dbname= 'postgres', host='localhost', 
        port= '5432', user= 'postgres', password= '123456')
        return con