from ...Resource.Context.ModelContext import ModelContext
from ...Domain.Entities.Topology import Topology

class WorldRepository:
    def GetWorld(self):
        top = Topology()
        context = ModelContext()
        con = context.ConnectionPostgreSql()
        cur = con.cursor()
        cur.execute('SELECT "Message" FROM public."MessageWorld"')
        db_version = cur.fetchone()
        cur.close()
        return db_version