#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) { //qsort 내림차순
    return *(int*)b - *(int*)a;
}

int solution(int k, int tangerine[], size_t tangerine_len) {
    int tangerines_by_size[10000000] = {0, };// 귤 사이즈 종류
    int answer = 0;

    for (int i = 0; i < tangerine_len; i++) { // 사이즈별 귤 개수
        tangerines_by_size[tangerine[i] - 1]++;
    }

    qsort(tangerines_by_size, 10000000, sizeof(int), compare); 
    //내림차순 정렬

    while (k > 0) {
        k -= tangerines_by_size[answer];
        answer++;
    }

    return answer;
}