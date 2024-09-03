#include <stdio.h>

int potenciacao(int n, int e){
    if(e == 0)
        return 1;
    return n * potenciacao(n, e-1);
}

int main(){
    int n = 5, e = 2;

    printf("%d", potenciacao(n, e));
}