#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int a, int b) {
    int answer = 0;
    int a_b = a*pow(10,floor(log10(b)+1))+b;
    answer = (a_b >= 2*a*b) ? a_b : 2*a*b;
    return answer;
}