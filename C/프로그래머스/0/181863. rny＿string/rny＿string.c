#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* rny_string) {
    int m_count = 0;
    for(int i = 0; i < strlen(rny_string); i++){
        if (rny_string[i] == 'm'){
            m_count++;
        }
    }
    // printf("%d\n", m_count);
    
    char* answer = (char*)calloc(strlen(rny_string)+m_count+2, sizeof(char));
    for(int i = 0, j = 0; i < strlen(rny_string); i++,j++){
        if (rny_string[i] == 'm'){
            answer[j] = 'r';
            answer[j+1] = 'n';
            j++;
        } else {
            answer[j] = rny_string[i];
        }
    }
    // printf("%s ", answer);
    return answer;
}