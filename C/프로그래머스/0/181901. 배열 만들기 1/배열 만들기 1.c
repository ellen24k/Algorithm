#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)calloc(n/k + 1, sizeof(int));
    int index = 0; int plus_val = 0;
    
    while (n >= plus_val) {
        plus_val += k;
        answer[index++] = plus_val;
    }
    return answer;
}