#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(strlen(s) + 1);
    strcpy(answer,s);
    printf(answer);
    
    for(int total_index = 0, word_index = 0; total_index < strlen(answer); total_index++) {        
        if(answer[total_index] == ' ') {
            word_index = 0;
            continue;
        }
        
        if(word_index%2==0) {
            if(answer[total_index] >= 'a') answer[total_index] -= 32;
        } else {
            if(answer[total_index] <= 'Z') answer[total_index] += 32;
        }
        word_index++;
    }
    
    return answer;
}