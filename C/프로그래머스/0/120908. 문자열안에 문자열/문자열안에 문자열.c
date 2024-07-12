#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* str1, const char* str2) {
    int answer = 0;
    
    for (int i = 0; i < strlen(str1)-strlen(str2) + 1; i++) {
        int is_included = 1;
        for(int j = 0; j < strlen(str2); j++) {
            if (str1[i+j] != str2[j]) {
                is_included = 0;
                break;
            }
        }
        if(is_included) return 1;
    }
    return 2;
}