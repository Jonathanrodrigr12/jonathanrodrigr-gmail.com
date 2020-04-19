#------------------------------------------------------
# Clase para la entidad de Device 
# Devices Actuales
#------------------------------------------------------

# Clase Device
class Device:

    # Constructor
    def __init__(self):

        #Propiedades de la entidad
        self.device_Identifier = int
        self.metering_Type = str
        self.serial_Number = str
        self.model = str
        self.brand = int
        self.description_Device = str
        self.account_Number = str
        self.status_Device = str
        self.category_Device = str
        self.device_Master_Id = str
        self.authentication_Level = str
        self.authentication_Password = str
        self.authentication_User = str
        self.connection_Type = str
        self.ip_Host_Name = str
        self.port = int
        self.telephone_Number = str
        self.communication_Address = str
        self.user_Of_Area_Code = bool
        self.area_Code = str
        self.communication_Manager = bool
        self.imei = int
        self.baud_Rate= int
        self.data_Bits = int
        self.stop_Bits = int
        self.parity = str
        self.data_Terminal_Ready = bool
        self.time_Out = int
        self.tries = int
        self.carrier_Detect = bool
        self.device_Comments = str
        self.frames_Per_Package = int
        self.ratio = str
        self.ratios_Primary = str
        self.ratios_Secondary = str
        self.ratios_Type = str
        self.request_To_Send = bool

    # Setter's y Getter's
    def set_Device_Identifier(self, device_Identifier):
        self.device_Identifier = device_Identifier

    def get_Device_Identifier(self):
        return self.device_Identifier    

    def set_Metering_Type(self, metering_Type):
        self.metering_Type = metering_Type

    def getmetering_Type(self):
        return self.metering_Type    
    
    def set_Serial_Number(self, serial_Number):
        self.serial_Number = serial_Number

    def get_Serial_Number(self):
        return self.serial_Number   

    def set_Model(self, model):
        self.model = model

    def get_Model(self):
        return self.model  

    def set_Brand(self, brand):
        self.brand = brand

    def get_Brand(self):
        return self.brand     

    def set_Description_Device(self, description_Device):
        self.description_Device = description_Device

    def get_Description_Device(self):
        return self.description_Device   

    def set_Account_Number(self, account_Number):
        self.account_Number = account_Number

    def get_Account_Number(self):
        return self.account_Number

    def set_Status_Device(self, status_Device):
        self.status_Device = status_Device

    def get_Status_Device(self):
        return self.status_Device 

    def set_Category_Device(self, category_Device):
        self.category_Device = category_Device

    def get_Category_Device(self):
        return self.category_Device  

    def set_Device_Master_Id(self, device_Master_Id):
        self.device_Master_Id = device_Master_Id

    def get_Device_Master_Id(self):
        return self.device_Master_Id           

    def set_Authentication_Level(self, authentication_Level):
        self.authentication_Level = authentication_Level

    def get_Authentication_Level(self):
        return self.authentication_Level 

    def set_Authentication_Password(self, authentication_Password):
        self.authentication_Password = authentication_Password

    def get_Authentication_Password(self):
        return self.authentication_Password      

    def set_Authentication_User(self, authentication_User):
        self.authentication_User = authentication_User

    def get_authentication_User(self):
        return self.authentication_User  

    def set_Connection_Type(self, connection_Type):
        self.connection_Type = connection_Type

    def get_Connection_Type(self):
        return self.connection_Type

    def set_Ip_Host_Name(self, ip_Host_Name):
        self.ip_Host_Name = ip_Host_Name

    def get_Ip_Host_Name(self):
        return self.ip_Host_Name

    def set_Port(self, port):
        self.port = port

    def get_Port(self):
        return self.port 

    def set_Telephone_Number(self, telephone_Number):
        self.telephone_Number = telephone_Number

    def get_Telephone_Number(self):
        return self.telephone_Number   
    
    def set_Communication_Address(self, communication_Address):
        self.communication_Address.append(communication_Address)

    def get_Communication_Address(self):
        return self.communication_Address

    def set_User_Area_Code(self, user_Area_Code):
        self.user_Of_Area_Code = user_Area_Code

    def get_User_Area_Code(self):
        return self.user_Of_Area_Code

    def set_Area_Code(self, area_Code):
        self.area_Code = area_Code

    def get_Area_Code(self):
        return self.area_Code

    def set_Communication_Manager(self, communication_Manager):
        self.communication_Manager = communication_Manager

    def get_Communication_Manager(self):
        return self.communication_Manager           

    def set_Imei(self, imei):
        self.imei = imei

    def get_Imei(self):
        return self.imei 

    def set_Baud_Rated(self, baud_Rate):
        self.baud_Rate = baud_Rate

    def get_Baud_Rated(self):
        return self.baud_Rate

    def set_Data_Bits(self, data_Bits):
        self.data_Bits = data_Bits

    def get_Data_Bits(self):
        return self.data_Bits

    def set_Stop_Bits(self, stop_Bits):
        self.stop_Bits = stop_Bits

    def get_Stop_Bits(self):
        return self.stop_Bits

    def set_Parity(self, parity):
        self.parity = parity

    def get_Parity(self):
        return self.parity 

    def set_Data_Terminal_Ready(self, data_Terminal_Ready):
        self.data_Terminal_Ready = data_Terminal_Ready

    def get_Data_Terminal_Ready(self):
        return self.data_Terminal_Ready_DTR 

    def set_Time_Out(self, time_Out):
        self.time_Out = time_Out

    def get_Time_Out(self):
        return self.time_Out_MS 

    def set_Tries(self, tries):
        self.tries = tries

    def get_Tries(self):
        return self.tries

    def set_Carrier_Detect(self, carrier_Detect):
        self.carrier_Detect = carrier_Detect

    def get_Carrier_Detect(self):
        return self.carrier_Detect

    def set_Device_Comments(self, device_Comments):
        self.device_Comments = device_Comments

    def get_Device_Comments(self):
        return self.device_Comments

    def set_Ratio(self, ratio):
        self.ratio = ratio

    def get_Ratio(self):
        return self.ratio

    def set_Ratios_Primary(self, ratios_Primary):
        self.ratios_Primary = ratios_Primary

    def get_Ratios_Primary(self):
        return self.ratios_Primary

    def set_Ratios_Secondary(self, ratios_Secondary):
        self.ratios_Secondary = ratios_Secondary

    def get_Ratios_Secondary(self):
        return self.ratios_Secondary

    def set_Ratios_Type(self, ratios_Type):
        self.ratios_Type = ratios_Type

    def get_Ratios_Type(self):
        return self.ratios_Type

    def set_Request_To_Send(self, request_To_Send):
        self.request_To_Send = request_To_Send

    def get_Request_To_Send(self):
        return self.request_To_Send                