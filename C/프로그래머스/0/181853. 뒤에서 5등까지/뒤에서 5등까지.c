#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(int* a, int* b) { // 오름차순
     return *a - *b;
}

int* solution(int num_list[], size_t num_list_len) {
    qsort(num_list,num_list_len,sizeof(int),compare);
    int* answer = (int*)malloc(5);
    
    for(int i = 0; i < 5; i++) {
        answer[i] = num_list[i];
    }
    
    return answer;
}