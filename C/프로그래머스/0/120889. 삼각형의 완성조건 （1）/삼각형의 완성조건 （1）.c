#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sides_len은 배열 sides의 길이입니다.
int solution(int sides[], size_t sides_len) {
    int total = 0;
    int max_side = 0;
    
    for (int i = 0; i < sides_len; i++) {
        total += sides[i];
        if (max_side < sides[i]) max_side = sides[i];
    }
    
    return (total - max_side > max_side) ? 1 : 2;
}