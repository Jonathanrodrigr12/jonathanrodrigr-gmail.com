#------------------------------------------------------
# Clase para la entidad de Agent
# Agent
#------------------------------------------------------

# Clase RelationDevice
class Agent:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.agentId = str
        self.agentDescription = str
        self.agentRole = [str]

    # Setter's y Getter's
    def set_Agent_Id(self, agentId):
        self.agentId = agentId

    def get_Agent_Id(self):
        return self.agentId    
    
    def set_Agent_Description(self, agentDescription):
        self.agentDescription = agentDescription

    def get_Agent_Description(self):
        return self.agentDescription 

    def set_Agent_Role(self, agentRole):
        self.agentRole = agentRole

    def get_Agent_Role(self):
        return self.agentRole       
