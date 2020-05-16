import sqlite3


class SqlLiteContext():

    @staticmethod
    def connect():
        try:
            con = sqlite3.connect('region.db')
            print("Connection is established: Database is created in memory")
            return con
        except Exception as Error:

            print(Error)
