#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, int m, int c) {
    char* answer = (char*)malloc(strlen(my_string) / m + 1);
    int idx = c-1;
    int ans_idx = 0;
    while (idx<strlen(my_string)) {
        answer[ans_idx] = my_string[idx];
        idx+=m;
        ans_idx++;
    }
    answer[ans_idx]='\0';
    return answer;
}