#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int answer = 0;
    
    for(int i = 0, num; i < strlen(s);){
        if(s[i] <= 57){ //숫자 48 ~ 57
            num = s[i] - '0';
            i++;
        } else {
            switch(s[i]) {
                case 'z':
                    num = 0;
                    i += 4;
                    break;
                case 'o':
                    num = 1;
                    i += 3;
                    break;
                case 't':
                    if(s[i+1] == 'w'){
                        num = 2;
                        i += 3;
                    } else {
                        num = 3;
                        i += 5;
                    }
                    break;
                case 'f':
                    if(s[i+1] == 'o'){
                        num = 4;
                    } else {
                        num = 5;
                    }
                    i += 4;
                    break;
                case 's':
                    if(s[i+1] == 'i'){
                        num = 6;
                        i += 3;
                    } else {
                        num = 7;
                        i += 5;
                    }
                    break;
                case 'e':
                    num = 8;
                    i += 5;
                    break;
                case 'n':
                    num = 9;
                    i += 4;
                    break;
            }
        }
        answer = answer * 10 + num;
    }
    
    
    return answer;
}