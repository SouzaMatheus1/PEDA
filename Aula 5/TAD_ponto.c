#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    float x;
    float y;
} Ponto;

Ponto* pontoCria(float x, float y){
    Ponto* p=(Ponto*) malloc(sizeof(Ponto));
    
    if(p == NULL){
        printf('Erro');
        exit(1);
    }

    p->x = x;
    p->y = y;
    return p;
}

void pontoAcessa(Ponto* p, float* x, float* y){
    if(p != NULL){
        *x = p->x;
        *y = p->y;
    }
}

void pontoAtribui(Ponto* p, float x, float y){
    if(p != NULL){
        p->x = x;
        p->y = y;
    }
}

void pontoDistancia(Ponto* p1, Ponto* p2){
    if(p1 != NULL && p2 != NULL){
        float dx = p1->x - p2->x;
        float dy = p1->y - p2->y;
    }
    return -1;
}

int main(){
    Ponto* ponto1 = pontoCria(1.0, 2.0);
    Ponto* ponto2 = pontoCria(3.0, 5.0);

    float x, y;
    pontoAcessa(ponto1, &x, &y);
    printf('%.2f, %.2f', &x, &y);
}