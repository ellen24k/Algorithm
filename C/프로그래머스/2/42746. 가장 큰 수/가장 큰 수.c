#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int compare(const void* a, const void* b) {
    int digit_of_a = 10;
    int digit_of_b = 10;
    while (*(int*)a >= digit_of_a) digit_of_a *= 10;
    while (*(int*)b >= digit_of_b) digit_of_b *= 10;
    
    int a_b = *(int*)a * digit_of_b + *(int*)b;
    int b_a = *(int*)b * digit_of_a + *(int*)a;
    return b_a-a_b; // 내림차순
}

char* solution(int numbers[], size_t numbers_len) {
    char* answer = (char*)malloc(numbers_len * 4 + 1);
    qsort(numbers, numbers_len, sizeof(int), compare);
    if(numbers[0] == 0) memcpy(answer,"0\0",2);
    else {
        long idx = 0;
        char* buffer = (char*)malloc(5);
        for (int i = 0; i < numbers_len; i++) {
            sprintf(buffer,"%d", numbers[i]);
            memcpy(&answer[idx], buffer, strlen(buffer)+1);
            idx += strlen(buffer);
        }
    }
    return answer;
}