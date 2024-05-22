#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
    int answer = 0;

    for (int i = 0; i < absolutes_len; i++) {
        answer += (signs[i] == true) ? absolutes[i] : -absolutes[i];
    }

    return answer;
}