class DivisaoPorZeroError(Exception):
    def __init__(self, divisor, 
                 msg = "Divisor invalido"):
        self.divisor = divisor
        self.msg = msg
        super().__init__(self, msg)