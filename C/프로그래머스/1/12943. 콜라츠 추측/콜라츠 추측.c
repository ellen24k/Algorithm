#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long num) {
    for (int i = 0; i < 501; i++) {
        if (num == 1) return i;
        num = (num % 2) ? (num * 3) + 1 : num / 2;
    }

    return -1;
}