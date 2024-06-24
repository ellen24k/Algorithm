#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    //나머지 연산 : (a + b) % m = ((a % m) + (b % m)) % m
    unsigned int n_2 = 0;
    unsigned int n_1 = 1;
    unsigned int answer;
    
    for(int i = 2; i<=n; i++){
        answer = (n_1%1234567 + n_2%1234567)%1234567;
        n_2 = n_1;
        n_1 = answer;
    }
    return answer;
}