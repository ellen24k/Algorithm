#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int connect(int a, int b) {
    char b_str[6];
    sprintf(b_str, "%d", b);
    //sprintf_s(b_str, 6, "%d", b);
    a = a*pow(10,strlen(b_str)); 
    return a + b;
}

int solution(int a, int b) {
    int a_b = connect(a, b);
    int b_a = connect(b, a);
    if (a_b >= b_a) {
        return a_b;
    }
    else {
        return b_a;
    }

}