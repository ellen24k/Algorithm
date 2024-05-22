#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* s) {
    int isOdd = strlen(s)%2;
    char* answer = (char*)malloc(2 + isOdd);
    if (isOdd) {
        strncpy(answer,&s[strlen(s)/2],1);
        answer[1] = '\0';
    } else {
        strncpy(answer,&s[strlen(s)/2 - 1],2);
        answer[2] = '\0';
    }
    return answer;
}