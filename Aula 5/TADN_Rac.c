#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int mdc(int a, int b) {
    // calcula max divisor comum
    if (b == 0) {
        return a;
    }
    return mdc(b, a % b);
}

int mmc(int a, int b) {
    // calcula min mult comum
    return (a * b) / mdc(a, b);
}

typedef struct {
    float N; // Numerador
    float D; // Denominador
} N_RAC;

N_RAC* n_rac_cria(float n, float d){
    if(d == 0){ // verificacao adicionada pela correçao
        printf("denominador n pode ser 0");
        exit(1);
    }
    N_RAC* num = (N_RAC*) malloc(sizeof(N_RAC));

    if(num == NULL){
        printf("erro ao alocar memoria");
        exit(1);
    }

    num->N = n;
    num->D = d;
    return num;
}

N_RAC* n_rac_soma(N_RAC* rac_1, N_RAC* rac_2){
    N_RAC* rac_resp = (N_RAC*) malloc(sizeof(N_RAC));

    if(rac_2 != NULL && rac_1 != NULL){ // caso denominador seja igual
        if(rac_1->D == rac_2->D){
            rac_resp->D = rac_1->D;
            rac_resp->N = rac_1->N + rac_2->N;
        }else if(rac_1->D != rac_2->D){ // caso denominador seja diferente
            float mmc_calc = mmc(rac_1->D, rac_2->D);
            rac_resp->D = mmc_calc;
            rac_resp->N = (mmc_calc / rac_1->D * rac_1->N) + (mmc_calc / rac_2->D * rac_2->N);
        }
    }

    return rac_resp;
}

N_RAC* n_rac_subtrai(N_RAC* rac_1, N_RAC* rac_2){
    N_RAC* rac_resp = (N_RAC*) malloc(sizeof(N_RAC));

    if(rac_2 != NULL && rac_1 != NULL){ // caso denominador seja igual
        if(rac_1->D == rac_2->D){
            rac_resp->D = rac_1->D;
            rac_resp->N = rac_1->N - rac_2->N;
        }else if(rac_1->D != rac_2->D){ // caso denominador seja diferente
            float mmc_calc = mmc(rac_1->D, rac_2->D);
            rac_resp->D = mmc_calc;
            rac_resp->N = (mmc_calc / rac_1->D * rac_1->N) - (mmc_calc / rac_2->D * rac_2->N);
        }
    }

    return rac_resp;
}

N_RAC* n_rac_multiplica(N_RAC* rac_1, N_RAC* rac_2){
    N_RAC* rac_resp = (N_RAC*) malloc(sizeof(N_RAC));

    if(rac_2 != NULL && rac_1 != NULL){ 
        rac_resp->D = rac_1->D * rac_2->D;
        rac_resp->N = rac_1->N * rac_2->N;
    }

    return rac_resp;
}

N_RAC* n_rac_divide(N_RAC* rac_1, N_RAC* rac_2){
    N_RAC* rac_resp = (N_RAC*) malloc(sizeof(N_RAC));

    if(rac_2 != NULL && rac_1 != NULL){ 
        rac_resp->N = rac_1->N * rac_2->D;
        rac_resp->D = rac_1->D * rac_2->N;
    }

    return rac_resp;
}

N_RAC* n_rac_simplifica(N_RAC* rac){
    if(rac != NULL){
        int divisor = mdc(rac->D, rac->N);
        rac->N /= divisor;
        rac->D /= divisor;

        // adicionado pela correçao
        if(rac->D < 0) {  // Garantir que o denominador seja positivo
            rac->N = -rac->N;
            rac->D = -rac->D;
        }
    }

    return rac;
}