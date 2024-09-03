#include <stdio.h>

int fibonacci(int n){
    if(n <= 2)
        return 1;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main(){
    int num = 10;
    
    for(int i = 0; i <= num; i++){
        printf("%d \n", fibonacci(i));
    }
}