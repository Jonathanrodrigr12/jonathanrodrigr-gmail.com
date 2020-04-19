from ...Domain.Entities.Topology import Topology
from ...Domain.Entities.Reading import Readings
from ...Domain.Entities.Device import Device
from ...Domain.Entities.RelationDevice import Relation_Device
from ...Domain.Entities.ServicePoint import Service_Point
from ...Domain.Entities.ServicePointVariable import Service_Point_Varible
from ...Domain.Entities.Owner import Owner

class Generic_Object_Service:
    def generic_Object_Response_Topology(self):
        toplogy = Topology()
        toplogy.set_Guid_Topology("d290f1ee-6c54-4b01-90e6")
        
        owner = Owner()
        owner.set_Hes("22")
        owner.set_Owner("asd")
        owner.set_Guid_File("123-123-qw123")

        device = Device()
        device.set_Device_Identifier(123)
        device.set_Metering_Type("MS123")
        device.set_Serial_Number('123-akdjd-234')
        device.set_Model('2019 enero')
        device.set_Brand('Maste')
        device.set_Description_Device('Device ION')
        device.set_Account_Number('991034')
        device.set_Status_Device('ON')
        device.set_Category_Device('Device 123')
        device.set_Device_Master_Id('Master 123')
        device.set_Authentication_Level('User system')
        device.set_Authentication_Password('919203')
        device.set_Authentication_User('System')
        device.set_Connection_Type('Red wifi')
        device.set_Ip_Host_Name('922.124.123')
        device.set_Port(9999)
        device.set_Telephone_Number('31422245')
        device.set_Communication_Address('31422245')
        device.set_User_Area_Code(False)
        device.set_Area_Code('asd123')
        device.set_Communication_Manager(True)
        device.set_Imei(1)
        device.set_Baud_Rated(123)
        device.set_Data_Bits(999)
        device.set_Stop_Bits(124)
        device.set_Parity(123)
        device.set_Data_Terminal_Ready(True)
        device.set_Time_Out(99)
        device.set_Tries(99)
        device.set_Carrier_Detect(True)
        device.set_Device_Comments('123aa')
        device.set_Ratio('888')
        device.set_Ratios_Primary('RRTT')
        device.set_Ratios_Secondary("12")
        device.set_Ratios_Type("12")
        device.set_Request_To_Send(True)

        ServicePointVariable = Service_Point_Varible()
        ServicePointVariable.set_Ke_Register(12)
        ServicePointVariable.set_Ct_Register(12)
        ServicePointVariable.set_Pt_Register(87)
        ServicePointVariable.set_Sf_Register(22)
        ServicePointVariable.set_Factor_Register(123)
        ServicePointVariable.set_Is_Register(True)
        ServicePointVariable.set_Channel(222)
        ServicePointVariable.set_Log_Number(222)
        ServicePointVariable.set_Uom_Measure("222")
        ServicePointVariable.set_Customer_Name("222")
        ServicePointVariable.set_Customer_Name("222")
        ServicePointVariable.set_Register_Last_Read("2019-01-01")
        ServicePointVariable.set_Profile_Last_Read("2019-01-01")
        ServicePointVariable.set_Events_Last_Read("2019-01-01")
        ServicePointVariable.set_Interval_Size(4570)
        ServicePointVariable.set_Ke_Profile(12)
        ServicePointVariable.set_Ct_Profile(12)
        ServicePointVariable.set_Pt_Profile(87)
        ServicePointVariable.set_Sf_Profile(22)
        ServicePointVariable.set_Factor_Profile(22)
        ServicePointVariable.set_Is_Profile(True)
        ServicePointVariable.set_Variable_Id(True)


        servicePoint = Service_Point()
        
        servicePoint.set_Description_Point('Device Principal')
        servicePoint.set_Identification_Point('99123KRM')
        
        relationDevice = Relation_Device()
        relationDevice.set_Master_Identifier_Device("123")
        relationDevice.set_Master_Identifier_Point("1234")
        relationDevice.set_Relation_Endt_Date("2019-01-01")
        relationDevice.set_Relation_Start_Date("2019-01-01")

        toplogy.set_Relation_Device(relationDevice)
        toplogy.set_Service_Point(servicePoint)
        toplogy.set_Service_Point_Variable(ServicePointVariable)
        toplogy.set_Device(device)
        toplogy.set_Owner(owner)
        return self.response_Model_Topology(toplogy)

    def response_Model_Topology(self, arguments): 
        data = {}
        relationDevice = []
        servicePoint = []
        deviceResponse = []
        servicePointVariable = []
        owner = {
            "hes": arguments.owner.hes,
            "owner": arguments.owner.owner,
            "guidFile": arguments.owner.guid_File
        }

        for relation_Device in arguments.relation_Device:
            data = {
                     "masterIdentifierDevice": relation_Device.master_Identifier_Device,
                     "masterIdentifierPoint": relation_Device.master_Identifier_Point,
                     "relationEndDate": relation_Device.relation_End_Date,
                     "relationStartDate": relation_Device.relation_Start_Date
                   }
            relationDevice.append(data)

        for service_Point in arguments.service_Point:
            data = {
                     "identificationPoint": service_Point.identification_Point,
                     "descriptionPoint": service_Point.description_Point,
                   }
            servicePoint.append(data)

        for service_Point_Variable in arguments.service_Point_Variable:
            data = {
                     "meteringTypeDevice": service_Point_Variable.metering_Type_Device,
                     "keReading": service_Point_Variable.ke_Reading,
                     "ctReading": service_Point_Variable.ct_Reading,
                     "prReading": service_Point_Variable.pt_Reading,
                     "sfReading": service_Point_Variable.sf_Reading,
                     "channelReading": service_Point_Variable.channel_Reading,
                     "logReading": service_Point_Variable.log_Reading,
                     "uomReading": service_Point_Variable.uom_Reading,
                     "customer": service_Point_Variable.customer,
                     "lastRead": service_Point_Variable.lastRead,
                   }
            servicePointVariable.append(data)

        for device in arguments.devices:
            data = {
                     "DeviceIdentifier":device.device_Identifier,
                     "Type": device.type,
                     "MeteringType": device.metering_Type,
                     "SerialNumber": device.serial_Number,
                     "model": device.model,
                     "brand": device.brand,
                     "DescriptionDevice": device.description_Device,
                     "AccountNumber": device.account_Number,
                     "StatusDevice": device.status_Device,
                     "CategoryDevice": device.category_Device,
                     "MaterId": device.device_Master_Id,
                     "ConnectionType": device.connection_Type,
                     "IpHostName": device.ip_Host_Name,
                     "Port": device.port,
                     "PhoneNumber": device.phone_Number,
                     "CommunicationAddres": device.communication_Address,
                     "UserAreaCode": device.user_Of_Area_Code,
                     "AreaCode": device.area_Code,
                     "CommunicationManager": device.communication_Manager,
                     "Imei": device.imei,
                     "SendPing": device.send_Ping,
                     "PingTime": device.ping_Time,
                     "UserEthernet": device.user_Ethernet,
                     "Ethernet": device.ethernet,
                     "VirlocDevice": device.virloc_Device,
                     "DataBits": device.data_Bits,
                     "StopBits": device.stop_Bits,
                     "Parity": device.parity
                   }
                   
            deviceResponse.append(data)          

        data = {
                "GuidTopology": arguments.guid_Topology,
                "Owner": owner,
                "RelationDevice": relationDevice,
                "ServicePoint": servicePoint,
                "ServicePointVariable": servicePointVariable,
                "Device": deviceResponse
               }   
        return data

    def generic_Object_Reading(self):
        reading = Readings()
        reading.set_Guid_Readings("123-123-qw123")
        reading.set_Identifier_Service_Point("asd123")
        reading.set_Type_Variable("UOAM")
        reading.set_Ident_Reading(22)
        reading.set_Ident_Event(22)
        reading.set_Id_Variablet(22)
        reading.set_Id_Vdi(22)
        reading.set_Device_Identifier("22")
        reading.set_Id_Date_YMD(20200121)
        reading.set_Id_Date_YW(2020014)
        reading.set_Date_Utc("2019-01-01")
        reading.set_Date_Source("2019-01-01")
        reading.set_Date_Creation("2019-01-01")
        reading.set_Flags_DST(33)
        reading.set_Channel(55)
        reading.set_Uom("KWR")
        reading.set_Validation_Flag("2>kr")
        reading.set_Interval(22)
        reading.set_Log_Number(22)
        reading.set_Multuplier_Values(22)
        reading.set_Raw_Reading(22)
        reading.set_Usage_Reading(22)
        reading.set_Usage_Valid("S2")
        reading.set_Estimation_Reading(2)
        reading.set_Estimation_Reading(2)
        reading.set_Estimation_Valid("22")
        reading.set_Edition_Reading(22)
        reading.set_Edition_Valid("22")
        reading.set_Hes("22")
        reading.set_Owner("asd")
        reading.set_Guid_File("123-123-qw123")
        reading.set_Status("ON")
        return self.response_Model_Reading(reading)

    def response_Model_Reading(self, arguments):
        data = {
            "guidReading": arguments.guid_Readings,
            "identifierServicePoint": arguments.identifier_Service_Point,
            "typeVariable": arguments.type_Variable,
            "identReading": arguments.ident_Reading,
            "identEvent": arguments.ident_Event,
            "idVariable": arguments.id_Variable,
            "idVdi": arguments.id_Vdi,
            "deviceIdentifier": arguments.device_Identifier,
            "idDateYMD": arguments.id_Date_YMD,
            "idDateYW": arguments.id_Date_YW,
            "dateUtc": arguments.date_Utc,
            "dateSource": arguments.date_Source,
            "dateLocal": arguments.date_Local,
            "dateCreation": arguments.date_Creation,
            "flagsDST": arguments.flags_DST,
            "channel": arguments.channel,
            "uom": arguments.uom,
            "validationFlag": arguments.validation_Flag,
            "interval": arguments.interval,
            "logNumber": arguments.log_Number,
            "multuplierValues": arguments.multuplier_Values,
            "rawReading": arguments.raw_Reading,
            "usageReading": arguments.usage_Reading,
            "usageValid": arguments.usage_Valid,
            "estimationReading": arguments.estimation_Reading,
            "estimationValid": arguments.estimation_Valid,
            "editionReading": arguments.edition_Reading,
            "editionValid": arguments.edition_Valid,
            "hes": arguments.hes,
            "owner": arguments.owner,
            "guidFile": arguments.guid_File,
            "status": arguments.status
        }

        return data