#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(int* a, int* b) { //오름차순
    return *a - *b;
}

int* solution(int num_list[], size_t num_list_len) {    
    int* answer = (int*)malloc(num_list_len-5);
    qsort(num_list, num_list_len, sizeof(int), compare);
    
    for (int i = 0; i < num_list_len-5; i++) {
        answer[i] = num_list[i+5];
        printf("%d ",answer[i]);
    }
    
    return answer;
}