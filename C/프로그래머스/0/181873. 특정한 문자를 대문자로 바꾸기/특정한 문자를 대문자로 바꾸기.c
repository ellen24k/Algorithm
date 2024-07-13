#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, const char* alp) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)calloc(strlen(my_string) + 1, sizeof(char));
    
    for (int i = 0; i < strlen(my_string); i++) {
        printf("%c %c\n", my_string[i], *alp);
        if (my_string[i] == *alp) {
            printf("%c\n",my_string[i]);
            answer[i] = *alp - ('a'-'A');
        } else answer[i] = my_string[i];
    }
    
    return answer;
}