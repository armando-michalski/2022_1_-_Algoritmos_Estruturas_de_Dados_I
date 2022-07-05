class Publicacao:

    def __init__(self, idP, dataP):
        self.__id = idP
        self.__data = dataP

    def setInformacoes(self, idP, dataP):
        self.__ide = idP
        self.__data = dataP

    def getInformacoes(self):
        return [self.__id, self.__data]

    def __str__(self):
        return "Id: " + self.__id + "\nData: " + self.__data 
