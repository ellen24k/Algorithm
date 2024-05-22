#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    answer = ((long)abs(a-b)+1)*(long)(a+b)/2;
    
    return answer;
}