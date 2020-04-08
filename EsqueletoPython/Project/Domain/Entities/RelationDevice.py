#------------------------------------------------------
# Clase para la entidad de Relation Device
# Relacion entre el dispositov y el punto de servicio
#------------------------------------------------------

#importancion
import datetime

# Clase RelationDevice
class Relation_Device:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.relation_Start_Date = datetime.datetime.now()
        self.relation_End_Date = datetime.datetime.now()
        self.master_Identifier_Device = str
        self.master_Identifier_Point = str

    # Setter's y Getter's
    def set_Relation_Start_Date(self, relation_Start_Date):
        self.relation_Start_Date = relation_Start_Date

    def get_Relation_Start_Date(self):
        return self.relation_Start_Date    
    
    def set_Relation_Endt_Date(self, relation_Endt_Date):
        self.relation_End_Date = relation_Endt_Date

    def get_Relation_Endt_Date(self):
        return self.relation_End_Date

    def set_Master_Identifier_Device(self, master_Identifier_Device):
        self.master_Identifier_Device = master_Identifier_Device

    def get_Master_Identifier_Device(self):
        return self.master_Identifier_Device 

    def set_Master_Identifier_Point(self, master_Identifier_Point):
        self.master_Identifier_Point = master_Identifier_Point

    def get_Master_Identifier_Point(self):
        return self.master_Identifier_Point        
