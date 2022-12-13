
class Docente():
    def __init__(self, nombre="", edad="", sueldo="", td=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__sueldo=sueldo
        self.__td=td #Tipo Docente

    def SetNombre(self, nombre):
        self.__nombre=nombre
    def GetNombre(self):
        return self.__nombre
    
    def SetEdad(self, edad):
        self.__edad=edad
    def GetEdad(self):
        return self.__edad
    
    def SetSueldo(self, sueldo):
        self.__sueldo=sueldo
    def GetSueldo(self):
        return self.__sueldo
    
    def SetTD(self, td):
        self.__td=td
    def GetTD(self):
        return self.__td