class Complexo:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def __add__(self, c):
        return Complexo(self.a + c.a, self.b + c.b)
    
    def __sub__(self, c):
        return Complexo(self.a - c.a, self.b - c.b)
    
    def __mul__(self, c):
        return Complexo(self.a * c.a, self.b * c.b)
    
    def __truediv__(self, c):
        if c.a == 0 and c.b == 0:
            return 'erro'
        denom = c.a ** 2 + c.b ** 2
        a = (self.a * c.a + self.b * c.b) / denom
        b = (self.b * c.a - self.a * c.b) / denom
        return Complexo(a, b)
    
    def __str__(self):
        return f"{self.a} + {self.b}i"
    
if __name__ == "__main__":
    c1 = Complexo(2,3)
    c2 = Complexo(1, -1)
    c = c1 + c2

    soma = c1 + c2
    subtracao = c1 - c2
    multiplicacao = c1 * c2
    divisao = c1 / c2

    print("c1 =", c1)
    print("c2 =", c2)
    print("Soma: c1 + c2 =", soma)
    print("Subtração: c1 - c2 =", subtracao)
    print("Multiplicação: c1 * c2 =", multiplicacao)
    print("Divisão: c1 / c2 =", divisao)