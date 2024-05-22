#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int numer1, int denom1, int numer2, int denom2) {
    int* answer = (int*)malloc( sizeof(int)*2 );

    int numer = (numer1*denom2) + (numer2*denom1);
    int denom = denom1*denom2;

    int min = (numer > denom) ? denom : numer;
    int current_dividing_val = 2;
    
    while (current_dividing_val <= min) {
        if (numer % current_dividing_val == 0 && 
            denom % current_dividing_val == 0) {
            numer /= current_dividing_val;
            denom /= current_dividing_val;
        }
        else current_dividing_val++;
    }
    answer[0] = numer;
    answer[1] = denom;

    return answer;
}