#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* str1, const char* str2) {
    int answer;
    
    for(int i = 0; i <= strlen(str2)-strlen(str1); i++) {
        answer = 1;
        for(int j = 0; j < strlen(str1); j++) {
            
            if (str1[j] != str2[i+j]) {
                answer = 0;
                break;
            }
        }
        if (answer == 1) return 1;
    }
    
    return 0;
}