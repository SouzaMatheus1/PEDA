public class N_RAC{
    private float numerador;
    private float denominador;

    public N_RAC(float n, float d){
        if(d == 0){
            throw new IllegalArgumentException("Erro! O denominador não pode ser 0.");
        }
        this.numerador = n;
        this.denominador = d;
    }

    public int mdc(int a, int b){
        if(b == 0){
            return a;
        }
        return mdc(b, a % b);
    }

    public int mmc(int a, int b){
        return (a * b) / mdc(a, b);
    }

    public N_RAC n_rac_criar(float n, float d){
        if(d == 0){
            throw new IllegalArgumentException("Erro! O denominador não pode ser 0.");
        }
        return new N_RAC(n, d);
    }

    public N_RAC n_rac_somar(N_RAC rac1, N_RAC rac2){
        N_RAC rac_result = new N_RAC(0, 1);

        if(rac1 != null && rac2 != null){
            if(rac1.denominador == rac2.denominador){
                rac_result.denominador = rac1.denominador;
                rac_result.numerador = rac1.numerador + rac2.numerador;
            }else{
                int mmc_calc = mmc((int) rac1.denominador, (int) rac2.denominador);
                rac_result.denominador = mmc_calc;
                rac_result.numerador = (mmc_calc / rac1.denominador * rac1.numerador) + (mmc_calc / rac2.denominador * rac2.numerador);
            }
        }
        return rac_result;
    }

    public N_RAC n_rac_subtrair(N_RAC rac1, N_RAC rac2){
        N_RAC rac_result = new N_RAC(0, 1);

        if(rac1 != null && rac2 != null){
            if(rac1.denominador == rac2.denominador){
                rac_result.denominador = rac1.denominador;
                rac_result.numerador = rac1.numerador - rac2.numerador;
            }else{
                int mmc_calc = mmc((int) rac1.denominador, (int) rac2.denominador);
                rac_result.denominador = mmc_calc;
                rac_result.numerador = (mmc_calc / rac1.denominador * rac1.numerador) - (mmc_calc / rac2.denominador * rac2.numerador);
            }
        }
        return rac_result;
    }

    public N_RAC n_rac_multiplicar(N_RAC rac1, N_RAC rac2){
        N_RAC rac_result = new N_RAC(0, 1);

        if(rac1 != null && rac2 != null){
            if(rac1.denominador == rac2.denominador){
                rac_result.denominador = rac1.denominador * rac2.denominador;
                rac_result.numerador = rac1.numerador * rac2.numerador;
            }
        }

        return rac_result;
    }

    public N_RAC n_rac_dividir(N_RAC rac1, N_RAC rac2){
        N_RAC rac_result = new N_RAC(0, 1);

        if(rac1 != null && rac2 != null){
            if(rac1.denominador == rac2.denominador){
                rac_result.numerador = rac1.numerador * rac2.numerador;
                rac_result.denominador = rac1.denominador * rac2.denominador;
            }
        }

        return rac_result;
    }

    public N_RAC n_rac_simplificar(N_RAC rac1){
        if(rac1 != null){
            int divisor = mdc((int) Math.abs(rac1.denominador), (int) Mat.abs(rac1.numerador));
            rac1.numerador /= divisor;
            rac1.denominador /= divisor;
        }

        return rac1;
    }

    public String toString() {
        return numerador + "/" + denominador;
    }
}