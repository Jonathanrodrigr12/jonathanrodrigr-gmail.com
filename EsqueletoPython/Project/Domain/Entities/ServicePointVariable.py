#------------------------------------------------------
# Clase para la entidad de Service Point Variable
# Para saber la asociación de variables con Punto de servicio
#------------------------------------------------------

# Importanciones
import datetime

# Clase ServicePointVariable
class Service_Point_Varible:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.metering_Type_Device = str
        self.ke_Reading = int
        self.ct_Reading = int
        self.pt_Reading = int
        self.sf_Reading = int
        self.channel_Reading = int
        self.log_Reading = int
        self.uom_Reading = str
        self.customer = str
        self.lastRead = datetime.datetime.now()

    # Setter's y Getter's
    def set_Metering_Type(self,metering_Type):
        self.metering_Type_Device = metering_Type

    def get_Metering_Type(self):
        return self.metering_Type_Device    
    
    def set_Ke_Reading(self, ke_Reading):
        self.ke_Reading = ke_Reading

    def get_Ke_Reading(self):
        return self.ke_Reading

    def set_Ct_Reading(self, ct_Reading):
        self.ct_Reading = ct_Reading

    def get_Ct_Reading(self):
        return self.ct_Reading

    def set_Pt_Reading(self,pt_Reading):
        self.pt_Reading = pt_Reading

    def get_Pt_Reading(self):
        return self.pt_Reading

    def set_Sf_Reading(self, sf_Reading):
        self.sf_Reading = sf_Reading

    def get_Sf_Reading(self):
        return self.get_Sf_Reading

    def set_Channel_Reading(self, channel_Reading):
        self.channel_Reading = channel_Reading

    def get_Channel_Reading(self):
        return self.channel_Reading

    def set_Log_Reading(self, log_Reading):
        self.log_Reading = log_Reading

    def get_Log_Reading(self):
        return self.log_Reading

    def set_Uom_Reading(self, uom_Reading):
        self.uom_Reading = uom_Reading

    def get_Uom_Reading(self):
        return self.uom_Reading

    def set_Customer(self, customer):
        self.customer = customer

    def get_Customer(self):
        return self.customer

    def set_Last_Read(self, last_Read):
        self.last_Read = last_Read

    def get_Last_Read(self):
        return self.last_Read                                

