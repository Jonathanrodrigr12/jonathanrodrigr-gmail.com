import pandas as pd

class TablePandaUtils():

    @staticmethod
    def create_table(table, column, connection):
        df = pd.DataFrame(table,columns=column,dtype=float) 
        df.to_sql("my_data", connection, if_exists="replace")
        print("completo el sql")
        print("Suma Total")
        print(df['time'].sum())
        print("Promedio ")
        print(df['time'].mean())
        print("Maximo ")
        print(df['time'].max())
        print("Minimo ")
        print(df['time'].min())
        df.to_json('./data/data.json', orient='records', lines=True)