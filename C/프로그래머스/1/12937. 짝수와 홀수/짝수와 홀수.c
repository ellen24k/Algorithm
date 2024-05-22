#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int num) {
    num = num % 2;
    char* answer = (char*)malloc(4 + num);
    answer = (num == 0) ? "Even\0" : "Odd\0";
    return answer;
}