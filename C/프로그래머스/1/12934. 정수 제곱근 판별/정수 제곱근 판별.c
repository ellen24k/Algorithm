#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

long long solution(long long n) {
    long long answer = -1;
    float sqrt_n = pow(n,0.5);
    if(sqrt_n-(int)sqrt_n ==0) answer = pow(sqrt_n+1,2);
    return answer;
}