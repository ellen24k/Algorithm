#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char* s) {
    int current_pair_state = 0; 

    while (*s) {
        if (s[0] == '(') {
            current_pair_state++;
        }
        else {
            current_pair_state--;
        }

        // 괄호는 )로 시작할 수 없음.
        if (current_pair_state < 0) return false; 
        
        *s++;
    }
    
    if (current_pair_state == 0 ) 
        return true;
    else
        return false;
    
}