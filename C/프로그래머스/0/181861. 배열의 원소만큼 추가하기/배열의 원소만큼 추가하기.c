#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int* solution(int arr[], size_t arr_len) {
    int count = 0;
    for (int i = 0; i < arr_len; i++){
        count += arr[i] * arr[i];
    }
    
    int* answer = (int*)malloc(count*sizeof(int));
    for(int i = 0, index=0; i < arr_len; i++){
        for(int j = 0; j < arr[i]; j++){
            answer[index++] = arr[i];
        }
    }
    
    return answer;
}