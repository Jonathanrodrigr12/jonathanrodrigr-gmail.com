#------------------------------------------------------
# Clase para la entidad de Quality
# Quality
#------------------------------------------------------

# Clase ServicePoint
class Quality:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.system_Id = str
        self.categorization = str
        self.index = int

    # Setter's y Getter's
    def set_System_Id(self, system_Id):
        self.system_Id = system_Id

    def get_System_Idt(self):
        return self.system_Id    
    
    def set_Categorization(self, categorization):
        self.categorization = categorization

    def get_Categorization(self):
        return self.categorization

    def set_Index(self, index):
        self.index = index

    def get_Index(self):
        return self.index    
