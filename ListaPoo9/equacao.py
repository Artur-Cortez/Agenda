class Equacao:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def __str__(self):
        return f"a - {self.__a} . b - {self.__b} . c - {self.__c}"
    def set_a(self, a):
        self.__a = a   
    def set_b(self, b):
        self.__b = b  
    def set_c(self, c):
        self.__c = c 
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def delta(self):
        return self.__b**2-4*self.__a*self.__c
    def TemRaizesReais(self):
        if self.delta() < 0:
            return False
        return True
    def Raiz1(self):
        return (-self.__b+self.delta()**0.5)/(2*self.__a)
    def Raiz2(self):
        return (-self.__b-self.delta()**0.5)/(2*self.__a)
    def y(self, x):
        return self.__a * x**2 + self.__b * x + self.__c 