#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, const char* letter) {
    // calloc은 메모리 할당과 동시에 초기화
    char* answer = (char*)calloc(strlen(my_string) + 1, 1);
        
    for (int i = 0, j = 0; i< strlen(my_string); i++) {
        if(my_string[i] != *letter) answer[j++] = my_string[i];
    }
    
    return answer;
}