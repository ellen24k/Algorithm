#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int n) {
    int answer = 0;
    int length = 0;
    int num = n;
    
    while(num>0){ //3진수로 변환했을 때의 자릿수 구하기
        length++;
        num /= 3;
    }
    
    for(int i = 1; i<=length; i++){ 
        answer += (n%3)*pow(3,length-i);
        n /= 3;
    }
    
    return answer;
}