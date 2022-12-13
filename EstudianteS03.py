
class Estudiante():
    def __init__(self, nombre="", edad="", fda="", curso):
        self.__nombre=nombre
        self.__edad=edad
        self.__fda=fda #Forma de Aprendizaje
        self.__curso=curso

    def SetNombre(self, nombre):
        self.__nombre=nombre
    def GetNombre(self):
        return self.__nombre

    def SetEdad(self, edad):
        self.__edad=edad
    def GetEdad(self):
        return self.__edad

    def SetFdA(self, fda):
        self.__fda=fda
    def GetFdA(self):
        return self.__fda

    def SetCurso(self, curso):
        self.__curso=curso
    def GetCurso(self):
        return self.__curso