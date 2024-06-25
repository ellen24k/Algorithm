#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// food_len은 배열 food의 길이
char* solution(int food[], size_t food_len) {
    int total_food = 1; // 물
    
    // 음식 개수 짝수로 맞추고 총 음식 개수 구하기
    for(int i = 1; i<food_len; i++){ 
        food[i] /= 2;
        total_food += food[i]*2;
    }
    
    char* answer = (char*)malloc(total_food + 1);
    answer[total_food] = '\0';
    
    //양쪽 끝을 기준으로 음식 배치
    for(int i = 1, first = 0, last = total_food -1 ; i < food_len; i++) { 
        for(int j = 0; j < food[i]; j++){
            answer[first++] = answer[last--] = i + '0';
        }
    }
    answer[total_food/2] = '0';
    

    return answer;
}