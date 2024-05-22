#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int i = 4;
    
    while(i<=n){
        if (i % 2 == 0) {
            answer++;
            i++;
        }
        for (int dividing_num = 3; dividing_num < i; dividing_num+=2) {
            if (i % dividing_num == 0) {
                answer++;
                break;
            }
        }
        i++;
    }
    return answer;
}