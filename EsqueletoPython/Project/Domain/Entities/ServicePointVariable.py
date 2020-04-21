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
        self.channel = int
        self.log_Number = int
        self.interval_Size = int
        self.ke_Register = int
        self.ct_Register = int
        self.pt_Register = int
        self.sf_Register = int
        self.factor_Register = int
        self.reading_Type = str
        self.profile_Last_Read = datetime.datetime.now()
        self.register_Number = str
        self.ke_Profile = int
        self.ct_Profile = int
        self.pt_Profile = int
        self.sf_Profile = int
        self.factor_Profile = int
        self.registers_Last_Read = datetime.datetime.now()
        self.events_Code = str
        self.events_Last_Read = datetime.datetime.now()
        self.variable_Id = bool
        self.customer_Name = str
        self.uom_Measure = str        

    # Setter's y Getter's 
    def set_Ke_Register(self, ke_Register):
        self.ke_Register = ke_Register

    def get_Ke_Register(self):
        return self.ke_Register

    def set_Ct_Register(self, ct_Register):
        self.ct_Register = ct_Register

    def get_Ct_Register(self):
        return self.ct_Register

    def set_Pt_Register(self,pt_Register):
        self.pt_Register = pt_Register

    def get_Pt_Register(self):
        return self.pt_Register

    def set_Sf_Register(self, sf_Register):
        self.sf_Register = sf_Register

    def get_Sf_Register(self):
        return self.get_Sf_Register

    def set_Factor_Register(self, factor_Register):
        self.factor_Register = factor_Register

    def get_Factor_Register(self):
        return self.factor_Register

    def set_Reading_Type(self, reading_Type):
        self.reading_Type = reading_Type

    def get_Reading_Type(self):
        return self.reading_Type           

    def set_Channel(self, channel):
        self.channel = channel

    def get_Channel(self):
        return self.channel

    def set_Log_Number(self, log_Number):
        self.log_Number = log_Number

    def get_Log_Number(self):
        return self.log_Number

    def set_Uom_Measure(self, uom_Measure):
        self.uom_Measure = uom_Measure

    def get_Uom_Measure(self):
        return self.uom_Measure

    def set_Customer_Name(self, customer_Name):
        self.customer_Name = customer_Name

    def get_Customer_Name(self):
        return self.customer_Name

    def set_Register_Last_Read(self, registers_Last_Read):
        self.registers_Last_Read = registers_Last_Read

    def get_Register_Last_Read(self):
        return self.registers_Last_Read 
    
    def set_Events_Code(self, events_Code):
        self.events_Code = events_Code

    def get_Events_Code(self):
        return self.events_Code 

    def set_Events_Last_Read(self, events_Last_Read):
        self.events_Last_Read = events_Last_Read

    def get_Events_Last_Read(self):
        return self.events_Last_Read

    def set_Profile_Last_Read(self, profile_Last_Read):
        self.profile_Last_Read = profile_Last_Read

    def get_Profile_Last_Read(self):
        return self.profile_Last_Read                                        
    
    def set_Register_Number(self, register_Number):
        self.register_Number = register_Number

    def get_Register_Number(self):
        return self.register_Number 
    
    def set_Interval_Size(self, interval_Size):
        self.interval_Size = interval_Size

    def get_Interval_Size(self):
        return self.interval_Size

    def set_Ke_Profile(self, ke_Profile):
        self.ke_Profile = ke_Profile

    def get_Ke_Profile(self):
        return self.ke_Profile

    def set_Ct_Profile(self, ct_Profile):
        self.ct_Profile = ct_Profile

    def get_Ct_Profile(self):
        return self.ct_Profile

    def set_Pt_Profile(self,pt_Profile):
        self.pt_Profile = pt_Profile

    def get_Pt_Profile(self):
        return self.pt_Profile

    def set_Sf_Profile(self, sf_Profile):
        self.sf_Profile = sf_Profile

    def get_Sf_Profile(self):
        return self.get_Sf_Profile

    def set_Factor_Profile(self, factor_Profile):
        self.factor_Profile = factor_Profile

    def get_Factor_Profile(self):
        return self.factor_Profile 

    def set_Variable_Id(self, variable_Id):
        self.variable_Id = variable_Id

    def get_Variable_Id(self):
        return self.variable_Id                
