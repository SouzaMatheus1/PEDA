import math

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return (a * b) // mdc(a, b)


class N_RAC():
    def __init__(self, numerador, denominador):
        if denominador == 0:
            print('erro! denominador nao pode ser 0')
        self.n = numerador
        self.d = denominador

    def n_rac_cria(n, d):
        if d == 0:
            print('erro! denominador nao pode ser 0')

        return N_RAC(n, d)

    def n_rac_soma(rac_1, rac_2):
        rac_resp = N_RAC(0, 1)

        if rac_1 is not None and rac_2 is not None:
            if rac_1.d == rac_2.d:
                rac_resp.d = rac_1.d
                rac_resp.n = rac_1.n + rac_2.n
            else:
                mmc_calc = mmc(rac_1.d, rac_2.d)
                rac_resp.d = mmc_calc
                rac_resp.n = (mmc_calc / rac_1.d * rac_1.n) + (mmc_calc / rac_2.d * rac_2.n)

        return rac_resp

    def n_rac_subtrai(rac_1, rac_2):
        rac_resp = N_RAC(0, 1)

        if rac_1 is not None and rac_2 is not None:  # caso denominador seja igual
            if rac_1.d == rac_2.d:
                rac_resp.d = rac_1.d
                rac_resp.n = rac_1.n - rac_2.n
            else:  # caso denominador seja diferente
                mmc_calc = mmc(rac_1.d, rac_2.d)
                rac_resp.d = mmc_calc
                rac_resp.n = (mmc_calc / rac_1.d * rac_1.n) - (mmc_calc / rac_2.d * rac_2.n)

        return rac_resp


    def n_rac_multiplica(rac_1, rac_2):
        rac_resp = N_RAC(0, 1)

        if rac_1 is not None and rac_2 is not None:
            rac_resp.d = rac_1.d * rac_2.d
            rac_resp.n = rac_1.n * rac_2.n

        return rac_resp

    def n_rac_divide(rac_1, rac_2):
        rac_resp = N_RAC(0, 1)

        if rac_1 is not None and rac_2 is not None:
            rac_resp.n = rac_1.n * rac_2.d
            rac_resp.d = rac_1.d * rac_2.n

        return rac_resp

    def n_rac_simplifica(rac):
        if rac is not None:
            divisor = mdc(abs(rac.d), abs(rac.n))
            rac.n /= divisor
            rac.d /= divisor

        return rac