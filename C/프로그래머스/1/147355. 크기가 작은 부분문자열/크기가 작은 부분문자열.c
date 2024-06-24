#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* t, const char* p) {
    int answer = 0;
    
    for(int index_t = 0; index_t<=strlen(t)-strlen(p);index_t++){
        if(t[index_t]>p[0]) continue;
        else {
            
            int is_equal = 0;
                
            for(int temp_t = index_t, temp_p = 0; temp_p < strlen(p); temp_t++, temp_p++) {
                
                if(t[temp_t]==p[temp_p]) is_equal = 1;
                else{
                    is_equal = 0;
                    answer = (t[temp_t]<p[temp_p]) ? answer + 1 : answer;
                    break;
                }
            }
            
            if(is_equal) answer++;
        }
    }
    
    return answer;
}