#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// strArr_len은 배열 strArr의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* strArr[], size_t strArr_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(strArr_len*sizeof(char*));
    for (int i = 0, ans_idx = 0; i < strArr_len; i++){
        if (!strstr(strArr[i], "ad")){
            char* new_elem = (char*)calloc(strlen(strArr[i]) + 1, sizeof(char));
            strcpy(new_elem, strArr[i]);
            answer[ans_idx++] = new_elem;
        } 
    }
    return answer;
}