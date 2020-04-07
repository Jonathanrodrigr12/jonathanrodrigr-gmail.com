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
        self.type = str
        self.metering_Type = str
        self.serial_Number = str
        self.model = str
        self.brand = int
        self.description_Device = str
        self.account_Number = str
        self.status_Device = str
        self.category_Device = str
        self.device_Master_Id = str
        self.remarks = str
        self.ct = str
        self.pt = str
        self.reading_User = str
        self.read_Password = str
        self.write_User = str
        self.write_Password = str
        self.connection_Type = []
        self.ip_Host_Name = str
        self.port = int
        self.phone_Number = str
        self.communication_Address = []
        self.user_Of_Area_Code = bool
        self.area_Code = str
        self.communication_Manager = bool
        self.imei = int
        self.send_Ping = bool
        self.ping_Time = int
        self.user_Ethernet = bool
        self.ethernet = str
        self.virloc_Device = str
        self.baud_Speed = []
        self.data_Bits = []
        self.stop_Bits = []
        self.parity = []
        self.data_Terminal_Ready_DTR = bool
        self.detect_Communication = bool
        self.ask_To_Send_RTS = bool
        self.time_Out_MS = int
        self.retries_Time = int
        self.frames_Per_Packet = int
        self.set_As_Default = str
        self.out_Put_Ports = str
        self.modem_Chains = str

    # Setter's y Getter's
    def set_Device_Identifier(self, device_Identifier):
        self.device_Identifier = device_Identifier

    def get_Device_Identifier(self):
        return self.device_Identifier    
    
    def set_Type(self, type):
        self.type = type

    def get_Type(self):
        return self.type

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

    def set_Remarks(self, remarks):
        self.remarks = remarks

    def get_Remarks(self):
        return self.remarks

    def set_Ct(self, ct):
        self.ct = ct

    def get_Ct(self):
        return self.ct  

    def set_Pt(self, pt):
        self.pt = pt

    def get_Pt(self):
        return self.pt

    def set_Reading_User(self, reading_User):
        self.reading_User = reading_User

    def get_Reading_User(self):
        return self.reading_User 

    def set_Read_Password(self, read_Password):
        self.read_Password = read_Password

    def get_Read_Password(self):
        return self.read_Password      

    def set_Write_User(self, write_User):
        self.write_User = write_User

    def get_Write_User(self):
        return self.write_User 

    def set_Write_Password(self, write_Password):
        self.write_Password = write_Password

    def get_Write_Password(self):
        return self.write_Password     

    def set_Connection_Type(self, connection_Type):
        self.connection_Type.append(connection_Type)

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

    def set_Phone_Number(self, phone_Number):
        self.phone_Number = phone_Number

    def get_Phone_Number(self):
        return self.phone_Number   

    def set_Communication_Address(self, communication_Address):
        self.communication_Address.append(communication_Address)

    def get_Communication_Address(self):
        return self.communication_Address 

    def set_Imei(self, imei):
        self.imei = imei

    def get_Imei(self):
        return self.imei

    def set_Send_Ping(self, send_Ping):
        self.send_Ping = send_Ping

    def get_Send_Ping(self):
        return self.send_Ping  

    def set_User_Ethernet(self, user_Ethernet):
        self.user_Ethernet = user_Ethernet

    def get_User_Ethernet(self):
        return self.user_Ethernet 

    def set_Ethernet(self, ethernet):
        self.ethernet = ethernet

    def get_Ethernet(self):
        return self.ethernet  

    def set_Virloc_Device(self, virloc_Device):
        self.virloc_Device = virloc_Device

    def getVirloc_Device(self):
        return self.virloc_Device    

    def set_Baud_Speed(self, baud_Speed):
        self.baud_Speed.append(baud_Speed)

    def get_Baud_Speed(self):
        return self.baud_Speed 

    def set_Data_Bits(self, data_Bits):
        self.data_Bits.append(data_Bits)

    def get_Data_Bits(self):
        return self.data_Bits

    def set_Stop_Bits(self, stop_Bits):
        self.stop_Bits.append(stop_Bits)

    def get_Stop_Bits(self):
        return self.stop_Bits

    def set_Parity(self, parity):
        self.parity.append(parity)

    def get_Parity(self):
        return self.parity 

    def set_Data_Terminal_Ready_DTR(self, data_Terminal_Ready_DTR):
        self.data_Terminal_Ready_DTR = data_Terminal_Ready_DTR

    def get_Data_Terminal_Ready_DTR(self):
        return self.data_Terminal_Ready_DTR 

    def set_Detect_Communication(self, detect_Communication):
        self.detect_Communication = detect_Communication

    def get_Detect_Communication(self):
        return self.detect_Communication 

    def set_Ask_To_Send_RTS(self, ask_To_Send_RTS):
        self.ask_To_Send_RTS = ask_To_Send_RTS

    def get_Ask_To_Send_RTS(self):
        return self.ask_To_Send_RTS

    def set_Time_Out_MS(self, time_Out_MS):
        self.time_Out_MS = time_Out_MS

    def get_Time_Out_MS(self):
        return self.time_Out_MS 

    def set_Retries_Time(self, retries_Time):
        self.retries_Time = retries_Time

    def get_Retries_Time(self):
        return self.retries_Time

    def set_Frames_Per_Packet(self, frames_Per_Packet):
        self.frames_Per_Packet = frames_Per_Packet

    def get_Frames_Per_Packet(self):
        return self.frames_Per_Packet

    def set_As_Default(self, set_As_Default):
        self.set_As_Default = set_As_Default

    def get_As_Default(self):
        return self.set_As_Default

    def set_Out_Put_Ports(self, out_Put_Ports):
        self.out_Put_Ports = out_Put_Ports

    def get_Out_Put_Ports(self):
        return self.out_Put_Ports

    def set_Modem_Chains(self, modem_Chains):
        self.modem_Chains = modem_Chains

    def get_Modem_Chains(self):
        return self.modem_Chains