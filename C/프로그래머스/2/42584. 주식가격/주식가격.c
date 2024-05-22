#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <memory.h>

int* solution(int prices[], size_t prices_len) {
    int* answer = (int*)malloc(sizeof(int)*prices_len);
    memset(answer, 0, sizeof(int) * prices_len);
    
    for (int i = 0; i < prices_len; i++) {
        for (int j = i+1; j < prices_len; j++) {
            answer[i]++;
            if (prices[i] > prices[j]) break;
        }
    }
    return answer;
}