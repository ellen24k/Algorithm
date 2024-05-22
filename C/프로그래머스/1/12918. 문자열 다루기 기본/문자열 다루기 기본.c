#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char* s) {
    if (strlen(s) == 4 || strlen(s) == 6) {
        while (*s) {
            if (65 <= (int)s[0] && (int)s[0] <= 122) return false;
            *s++;
        }
    } else return false;

    return true;
}