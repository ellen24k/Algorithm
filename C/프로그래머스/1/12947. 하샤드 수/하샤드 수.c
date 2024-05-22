#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    char x_str[6];
    sprintf(x_str, "%d", x);

    int sum_of_digits = 0;
    for (int i = 0; i < strlen(x_str); i++) {
        sum_of_digits += (char)x_str[i]-48; //아스키
    }

    return (x%sum_of_digits ==0)? true : false;
}