#------------------------------------------------------
# Clase para la entidad de Topology 
# Topology Actuales
#------------------------------------------------------

# Clase Topology
class Topology:

    # Constructor
    def __init__(self):
        #Propiedades de la entidad
        self.guid_Topology = str
        self.owner = {}
        self.service_Point_Variable = []
        self.service_Point = []
        self.devices = []
        self.relation_Device = []

    # Setter's y Getter's
    def set_Guid_Topology(self, guid_Topology):
        self.guid_Topology = guid_Topology

    def get_Guid_Topology(self):
        return self.guid_Topology    
    
    def set_Service_Point_Variable(self, service_Point_Variable):
        self.service_Point_Variable.append(service_Point_Variable)

    def get_Service_Point_Variable(self):
        return self.service_Point_Variable

    def set_Service_Point(self, service_Point):
        self.service_Point.append(service_Point)

    def get_Service_Point(self):
        return self.service_Point

    def set_Device(self, device):
        self.devices.append(device)

    def get_Device(self):
        return self.devices        
    
    def set_Relation_Device(self, relation_Device):
        self.relation_Device.append(relation_Device)

    def get_Relation_Device(self):
        return self.relation_Device

    def set_Owner(self, owner):
        self.owner = owner

    def get_Owner(self):
        return self.owner       