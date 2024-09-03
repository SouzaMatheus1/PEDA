#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int *data;
    int topo;
    int capacidade;
} Pilha;

Pilha* cria_pilha(int capacidade){
    Pilha* pilha = (Pilha*) malloc(sizeof(Pilha));
    pilha->capacidade = capacidade;
    pilha->topo = -1; // pilha começa vazia, ao add vai pra 0
    pilha->data = (int*) malloc(capacidade * sizeof(int));

    return pilha;
}

bool is_empty(Pilha* pilha){
    return pilha->topo == -1;
}

void push(Pilha* pilha, int el){
    if(is_empty(pilha)){
        printf("Lista cheia!");
        return;
    }

    pilha->data[++pilha->topo] = el;
}

void pop(Pilha* pilha, int el){
    if(is_empty(pilha)){
        printf("lista cheia");
        return;
    }

    return pilha->data[pilha->topo --];
}