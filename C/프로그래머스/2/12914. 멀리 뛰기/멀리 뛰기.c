#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int n) {
    int n_2 = 0;
    int n_1 = 1;
    int answer;
    
    
    for(int i = 0; i<n; i++){
        answer = (n_1%1234567 + n_2%1234567)%1234567;
        n_2 = n_1;
        n_1 = answer;
    }
    
    return answer;
}