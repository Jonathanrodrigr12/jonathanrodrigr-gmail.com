import psycopg2

class ModelContext():
    def ConnectionPostgreSql(self):
        con=psycopg2.connect(dbname= 'sample', host='database-2.cju1gt1fztf3.us-east-1.rds.amazonaws.com', 
        port= '5432', user= 'postgres', password= '12345678')
        return con