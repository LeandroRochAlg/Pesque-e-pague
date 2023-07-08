class Peixe:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    def getPeixe(self):
        return self.__nome + " - " + self.__preco
    
class PeixeComanda:
    def __init__(self, Peixe, peso):
        self.__Peixe = Peixe
        self.__peso = peso

    @property
    def Peixe(self):
        return self.__Peixe
    
    @property
    def peso(self):
        return self.__peso
    
    def getPeixeComanda(self):
        return self.__Peixe + " - " + self.__peso