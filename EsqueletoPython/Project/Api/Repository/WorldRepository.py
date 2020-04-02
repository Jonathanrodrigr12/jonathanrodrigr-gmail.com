from ...Resource.Context.ModelContext import ModelContext

class WorldRepository:
    def GetWorld(self):
        context = ModelContext()
        con = context.ConnectionPostgreSql()
        cur = con.cursor()
        cur.execute('SELECT "Message" FROM public."MessageWorld"')
        db_version = cur.fetchone()
        cur.close()
        return db_version