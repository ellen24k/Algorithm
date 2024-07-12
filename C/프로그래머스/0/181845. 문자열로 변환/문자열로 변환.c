#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)calloc(6,sizeof(char));
    int i = 0;
    
    int c = n;
    while(c>0) {
        c /= 10;
        i++;
    }
    
    for (int j = i-1; j >= 0; j--) {
        answer[j] = n%10 + '0';
        n /= 10;
    }
    
    return answer;
}