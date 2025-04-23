class Conjunto:

    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto) == 0:
            return 0  # o podrías lanzar una excepción si prefieres
        return sum(self.__conjunto) / len(self.__conjunto)