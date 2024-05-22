#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int compare(const char* a, const char* b) {
        return (*b - *a);    // 내림차순
}

char* solution(const char* s) {
    char* answer = (char*)malloc(strlen(s)+1);
    qsort(s, strlen(s), 1, compare);
    memcpy(answer, s, strlen(s));
    answer[strlen(s)] = '\0';
    return answer;
}