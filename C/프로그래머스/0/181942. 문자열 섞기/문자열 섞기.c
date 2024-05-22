#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* str1, const char* str2) {
    char* answer = (char*)malloc(strlen(str1)*2+1);
    int len = strlen(str1);

    int answer_index = 0;
    for (int i = 0; i < len; i++) {
        answer[answer_index] = str1[i];
        answer[answer_index+1] = str2[i];
        answer_index += 2;
    }
    answer[answer_index] = 0x00;
    return answer;
}