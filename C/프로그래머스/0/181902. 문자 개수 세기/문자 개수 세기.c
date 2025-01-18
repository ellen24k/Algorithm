#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int* solution(const char* my_string) {
    int* answer = (int*)malloc(52*sizeof(int));
    memset(answer, 0, 52*sizeof(int));
    while(*my_string){
        answer[(my_string[0] >= 'a') ? my_string[0] - 'a' + 26 : my_string[0] - 'A']++;
        my_string++;
    }
    return answer;
}