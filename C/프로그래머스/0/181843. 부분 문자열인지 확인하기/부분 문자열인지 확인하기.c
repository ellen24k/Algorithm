#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* target) {
    
    if (strlen(my_string) > strlen(target)) {
        for (int i = 0, is_true = -1; i < strlen(my_string); i++) {
            is_true = 1;
            for (int j = 0; j < strlen(target); j++) {
                if (target[j] != my_string[i+j]) {
                    // printf("%d %d\n", target[j], my_string[i+j]);
                    is_true = 0;
                    break;
                }
            }
            if  (is_true == 1) return 1;
        }
        return 0;
        
    } else if (strlen(my_string) == strlen(target)) {
        return strcmp(my_string,target) ? 0 : 1;
        
    } else {
        return 0;
    }
}