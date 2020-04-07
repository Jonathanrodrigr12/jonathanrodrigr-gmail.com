#------------------------------------------------------
# Clase para la entidad de Service Point 
# Puntos de servicio Actuales
#------------------------------------------------------

# Clase ServicePoint
class Service_Point:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.identification_Point = int
        self.description_Point = str

    # Setter's y Getter's
    def set_Identification_Point(self, identification_Point):
        self.identification_Point = identification_Point

    def get_Identification_Point(self):
        return self.metering_Type_Device    
    
    def set_Description_Point(self, description_Point):
        self.description_Point = description_Point

    def get_Description_Point(self):
        return self.description_Point
