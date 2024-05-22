#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return *(int*)a - *(int*)b;    // 오름차순
}

int solution(int A[], size_t A_len, int B[], size_t B_len) {
    int answer = 0;

    qsort(A, A_len, sizeof(int), compare);
    qsort(B, B_len, sizeof(int), compare);

    for (int i = 0; i < A_len; i++) {
        answer += A[i] * B[B_len - 1 - i];
    }

    return answer;
}