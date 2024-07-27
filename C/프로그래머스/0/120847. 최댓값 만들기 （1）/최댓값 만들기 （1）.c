#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int max = 0, sec = 0;
    
    for (int i = 0; i < numbers_len; i++){
        if (numbers[i] >= max){
            sec = max;
            max = numbers[i];
        } else if (numbers[i] > sec){
            sec = numbers[i];
        }
    }
    
    return max * sec;
}