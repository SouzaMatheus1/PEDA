class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def area(self):
        return self.ladoA * self.ladoB
    
    def perimetro(self):
        return 2 * (self.ladoA + self.ladoB)
    
    def __str__(self):
        return f"a={self.ladoA}; b={self.ladoB}; per={self.perimetro()}; area={self.area()}"