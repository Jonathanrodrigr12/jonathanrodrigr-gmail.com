#------------------------------------------------------
# Clase para la entidad de Readings
# Readings
#------------------------------------------------------

#importancion
import datetime

# Clase RelationDevice
class Readings:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.guid_Readings = str
        self.identifier_Service = str
        self.fount = str
        self.type = str
        self.version_Identifier = int
        self.date_UTC = datetime.datetime.now()
        self.variable = str
        self.identifier_Device = str
        self.date = datetime.datetime.now()
        self.date_Initial = datetime.datetime.now()
        self.date_Local = datetime.datetime.now()
        self.flag_DST = str
        self.identifier_Canal = int
        self.uom = str
        self.flags = str
        self.interval = str
        self.date_Creation = datetime.datetime.now()
        self.identifier_Log = int
        self.id = int
        self.event_Id = int
        self.id_Reanding = int
        self.value_Initial = int
        self.usage = str
        self.validation_Usage = str
        self.estimated = str
        self.validation_Estimated = str
        self.edited = str
        self.validation_Edited = str
        self.state = str

    # Setter's y Getter's
    def set_Guid_Readings(self, guid_Readings):
        self.guid_Readings = guid_Readings

    def get_Guid_Readings(self):
        return self.guid_Readings

    def set_Identifier_Service(self, identifier_Service):
        self.identifier_Service = identifier_Service

    def get_Identifier_Service(self):
        return self.identifier_Service

    def set_Fount(self, fount):
        self.fount = fount

    def get_Fount(self):
        return self.fount   

    def set_Type(self, type):
        self.type = type

    def get_Type(self):
        return self.type

    def set_Version_Identifier(self, version_Identifier):
        self.version_Identifier = version_Identifier

    def get_Version_Identifier(self):
        return self.version_Identifier

    def set_Date_UTC(self, date_UTC):
        self.date_UTC = date_UTC

    def get_Date_UTC(self):
        return self.date_UTC

    def set_Variable(self, variable):
        self.variable = variable

    def get_Variable(self):
        return self.variable

    def set_Identifier_Device(self, identifier_Device):
        self.identifier_Device = identifier_Device

    def get_Identifier_Device(self):
        return self.identifier_Device

    def set_Date(self, date):
        self.date = date

    def get_Date(self):
        return self.date

    def set_Date_Initial(self, date_Initial):
        self.date_Initial = date_Initial

    def get_Date_Initial(self):
        return self.date_Initial

    def set_Date_Local(self, date_Local):
        self.date_Local = date_Local

    def get_Date_Local(self):
        return self.date_Local

    def set_Flag_DST(self, flag_DST):
        self.flag_DST = flag_DST

    def get_Flag_DST(self):
        return self.flag_DST  

    def set_Identifier_Canal(self, identifier_Canal):
        self.identifier_Canal = identifier_Canal

    def get_Identifier_Canal(self):
        return self.identifier_Canal                       

    def set_UOM(self, uom):
        self.uom = uom

    def get_UOM(self):
        return self.uom

    def set_Flags(self, flags):
        self.flags = flags

    def get_Flags(self):
        return self.flags

    def set_Inteval(self, interval):
        self.interval = interval

    def get_Inteval(self):
        return self.interval 

    def set_Date_Creation(self, date_Creation):
        self.date_Creation = date_Creation

    def get_Date_Creation(self):
        return self.date_Creation

    def set_Identifier_Log(self, identifier_Log):
        self.identifier_Log = identifier_Log

    def get_Identifier_Log(self):
        return self.identifier_Log

    def set_Id(self, id):
        self.id = id

    def get_Id(self):
        return self.id

    def set_Event_Id(self, event_Id):
        self.event_Id = event_Id

    def get_Event_Id(self):
        return self.event_Id

    def set_Id_Reading(self, id_Reanding):
        self.id_Reanding = id_Reanding

    def get_Id_Reading(self):
        return self.id_Reanding

    def set_Value_Initial(self, value_Initial):
        self.value_Initial = value_Initial

    def get_Value_Initial(self):
        return self.value_Initial

    def set_Usage(self, usage):
        self.usage = usage

    def get_Usage(self):
        return self.usage 

    def set_Usage(self, usage):
        self.usage = usage

    def get_Usage(self):
        return self.usage 

    def set_Validation_Usage(self, validation_Usage):
        self.validation_Usage = validation_Usage

    def get_Validation_Usage(self):
        return self.validation_Usage

    def set_Estimated(self, estimated):
        self.estimated = estimated

    def get_Estimated(self):
        return self.estimated

    def set_Validation_Estimated(self, validation_Estimated):
        self.validation_Estimated = validation_Estimated

    def get_Validation_Estimated(self):
        return self.validation_Estimated

    def set_Edited(self, edited):
        self.edited = edited

    def get_Edited(self):
        return self.edited 

    def set_Validation_Edited(self, validation_Edited):
        self.validation_Edited = validation_Edited

    def get_Validation_Edited(self):
        return self.validation_Edited

    def set_State(self, state):
        self.state = state

    def get_State(self):
        return self.state                                                                                                    