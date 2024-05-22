#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return *(int*)a - *(int*)b;    // 오름차순
}

int solution(int weights[], size_t weights_len) {
    long answer = 0;

    qsort(weights, weights_len, sizeof(int), compare); // weights 오름차순 정렬

    for (int i1 = 0; i1 < weights_len - 1; i1++) {
        for (int i2 = i1 + 1; i2 < weights_len; i2++) {
            
            if (weights[i1] == weights[i2]) answer +=1;
            
            else if (weights[i1] * 4 >= weights[i2] * 2) {
                for (int distance1 = 3; distance1 <= 4; distance1++){
                    if (weights[i1] * distance1 == weights[i2] * 2){
                        answer +=1;
                        break;
                    } else if (weights[i1] * distance1 == weights[i2] * 3){
                        answer +=1;
                        break;
                    }
                }
            }
        }
    }
    return answer;
}