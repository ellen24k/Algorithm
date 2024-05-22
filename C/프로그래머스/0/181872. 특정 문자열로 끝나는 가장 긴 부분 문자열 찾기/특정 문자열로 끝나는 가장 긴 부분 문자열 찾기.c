#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString, const char* pat) {
    int idx = strlen(myString);
    while (strncmp(&myString[idx - strlen(pat)], pat, strlen(pat))) idx--;

    char* answer = (char*)malloc(idx);
    strncpy(answer, myString, idx);
    answer[idx] = '\0';
    return answer;
}