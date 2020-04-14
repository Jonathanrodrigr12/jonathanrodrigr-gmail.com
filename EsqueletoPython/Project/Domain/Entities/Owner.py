#------------------------------------------------------
# Clase para la entidad de Owner 
# Owner
#------------------------------------------------------

# Clase Owner
class Owner:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.hes = str
        self.owner = str
        self.guid_File = str
        

    # Setter's y Getter's
    def set_Hes(self, hes):
        self.hes = hes

    def get_Hes(self):
        return self.hes 

    def set_Owner(self, owner):
        self.owner = owner

    def get_Owner(self):
        return self.owner

    def set_Guid_File(self, guid_File):
        self.guid_File = guid_File

    def get_Guid_File(self):
        return self.guid_File                                                
                                                                          