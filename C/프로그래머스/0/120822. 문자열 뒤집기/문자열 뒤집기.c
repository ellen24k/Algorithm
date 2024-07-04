#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string) {    
    char* answer = (char*)malloc(strlen(my_string) + 1);
    answer[strlen(my_string)] = '\0';
    
    for (int i = strlen(my_string)-1, j = 0; i >= 0; i--, j++) {
        answer[i] = my_string[j];
    }
    
    return answer;
}