#------------------------------------------------------
# Clase para la entidad de Readings 
# Readings
#------------------------------------------------------
import datetime

# Clase Readings
class Readings:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.guid_Readings = str
        self.identifier_Service_Point = str
        self.reading_Type = str
        self.ident_Reading = int
        self.ident_Event = int
        self.id_Variable = str
        self.id_Vdi = int
        self.device_Identifier = str
        self.metering_Type = int
        self.id_Date_YMD = int
        self.id_Date_YW = int
        self.date_Utc = datetime.datetime.now()
        self.date_Source = datetime.datetime.now()
        self.date_Local = datetime.datetime.now()
        self.date_Creation = datetime.datetime.now()
        self.flags_DST = bool
        self.channel = int
        self.uom = str
        self.validation_Flag = []
        self.interval_Size = int
        self.log_Number = int
        self.multuplier_Values = []
        self.version = int
        self.raw_Reading = int
        self.usage_Reading = int
        self.usage_Valid = str
        self.estimation_Reading = int
        self.estimation_Valid = str
        self.edition_Reading = int
        self.edition_Valid = str
        self.primary_Source = str
        self.reading_Source = str
        self.owner = str
        self.guid_File = str
        self.status = str
        self.register_Number = str
        self.event_Code = str
        self.agent_Id = str
        self.aditional_Information = str

    # Setter's y Getter's
    def set_Guid_Readings(self, guid_Readings):
        self.guid_Readings = guid_Readings

    def get_Guid_Readings(self):
        return self.guid_Readings

    def set_Identifier_Service_Point(self, identifier_Service_Point):
        self.identifier_Service_Point = identifier_Service_Point

    def get_Identifier_Service_Point(self):
        return self.identifier_Service_Point

    def set_Reading_Type(self, reading_Type):
        self.reading_Type = reading_Type

    def get_Reading_Type(self):
        return self.reading_Type

    def set_Ident_Reading(self, ident_Reading):
        self.ident_Reading = ident_Reading

    def get_Ident_Reading(self):
        return self.ident_Reading

    def set_Ident_Event(self, ident_Event):
        self.ident_Event = ident_Event

    def get_Ident_Event(self):
        return self.ident_Event

    def set_Id_Variablet(self, id_Variable):
        self.id_Variable = id_Variable

    def get_Id_Variable(self):
        return self.id_Variable

    def set_Id_Vdi(self, id_Vdi):
        self.id_Vdi = id_Vdi

    def get_Id_Vdi(self):
        return self.id_Vdi

    def set_Device_Identifier(self, device_Identifier):
        self.device_Identifier = device_Identifier

    def get_Device_Identifier(self):
        return self.device_Identifier

    def set_Metering_Type(self, metering_Type):
        self.metering_Type = metering_Type

    def get_Metering_Type(self):
        return self.metering_Type

    def set_Id_Date_YMD(self, id_Date_YMD):
        self.id_Date_YMD = id_Date_YMD

    def get_Id_Date_YMD(self):
        return self.id_Date_YMD

    def set_Id_Date_YW(self, id_Date_YW):
        self.id_Date_YW = id_Date_YW

    def get_Id_Date_YW(self):
        return self.id_Date_YW

    def set_Date_Utc(self, date_Utc):
        self.date_Utc = date_Utc

    def get_Date_Utc(self):
        return self.date_Utc

    def set_Date_Source(self, date_Source):
        self.date_Source = date_Source

    def get_Date_Source(self):
        return self.date_Source

    def set_Date_Local(self, date_Local):
        self.date_Local = date_Local

    def get_Date_Local(self):
        return self.date_Local

    def set_Date_Creation(self, date_Creation):
        self.date_Creation = date_Creation

    def get_Date_Creation(self):
        return self.date_Creation

    def set_Flags_DST(self, flags_DST):
        self.flags_DST = flags_DST

    def get_Flags_DST(self):
        return self.flags_DST

    def set_Channel(self, channel):
        self.channel = channel

    def get_Channel(self):
        return self.channel

    def set_Uom(self, uom):
        self.uom = uom

    def get_Uom(self):
        return self.uom
    
    def set_Validation_Flag(self, validation_Flag):
        self.validation_Flag.append(validation_Flag)

    def get_Validation_Flag(self):
        return self.validation_Flag

    def set_Interval_Size(self, interval_Size):
        self.interval_Size = interval_Size

    def get_Interval_Size(self):
        return self.interval_Size

    def set_Log_Number(self, log_Number):
        self.log_Number = log_Number

    def get_Log_Number(self):
        return self.log_Number

    def set_Multuplier_Values(self, multuplier_Values):
        self.multuplier_Values.append(multuplier_Values)

    def get_Multuplier_Values(self):
        return self.multuplier_Values

    def set_Version(self, version):
        self.version = version

    def get_Verison(self):
        return self.version    

    def set_Raw_Reading(self, raw_Reading):
        self.raw_Reading = raw_Reading

    def get_Raw_Reading(self):
        return self.raw_Reading 

    def set_Usage_Reading(self, usage_Reading):
        self.usage_Reading = usage_Reading

    def get_Usage_Reading(self):
        return self.usage_Reading

    def set_Usage_Valid(self, usage_Valid):
        self.usage_Valid = usage_Valid

    def get_Usage_Valid(self):
        return self.usage_Valid

    def set_Estimation_Reading(self, estimation_Reading):
        self.estimation_Reading = estimation_Reading

    def get_Estimation_Reading(self):
        return self.estimation_Reading

    def set_Estimation_Valid(self, estimation_Valid):
        self.estimation_Valid = estimation_Valid

    def get_Estimation_Valid(self):
        return self.estimation_Valid

    def set_Edition_Reading(self, edition_Reading):
        self.edition_Reading = edition_Reading

    def get_Edition_Reading(self):
        return self.edition_Reading

    def set_Edition_Valid(self, edition_Valid):
        self.edition_Valid = edition_Valid

    def get_Edition_Valid(self):
        return self.edition_Valid
    
    def set_Primary_Source(self, primary_Source):
        self.primary_Source = primary_Source

    def get_Primary_Source(self):
        return self.primary_Source

    def set_Reading_Source(self, reading_Source):
        self.reading_Source = reading_Source

    def get_Reading_Source(self):
        return self.reading_Source 

    def set_Owner(self, owner):
        self.owner = owner

    def get_Owner(self):
        return self.owner

    def set_Guid_File(self, guid_File):
        self.guid_File = guid_File

    def get_Guid_File(self):
        return self.guid_File 

    def set_Status(self, status):
        self.status = status

    def get_Status(self):
        return self.status   

    def set_Register_Number(self, register_Number):
        self.register_Number = register_Number

    def get_Register_Number(self):
        return self.register_Number

    def set_Event_Code(self, event_Code):
        self.event_Code = event_Code

    def get_Event_Code(self):
        return self.event_Code  

    def set_Agent_Id(self, agent_Id):
        self.agent_Id = agent_Id

    def get_Agent_Id(self):
        return self.agent_Id 

    def set_Aditional_Information(self, aditional_Information):
        self.aditional_Information = aditional_Information

    def get_Aditional_Information(self):
        return self.aditional_Information                                                           
                                                                          