#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, const char* overwrite_string, int s) {
    char* answer = (char*)malloc(strlen(my_string)+1);
    strcpy(answer, my_string);
    
    while (*overwrite_string) {
        answer[s] = overwrite_string[0];
        *overwrite_string++;
        s++;
    }
    return answer;
}