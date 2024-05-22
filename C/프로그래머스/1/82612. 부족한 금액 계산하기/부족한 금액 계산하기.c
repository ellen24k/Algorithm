#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long price, long money, long count) {
    long long answer = price*(count*(count+1)/2);
    return (answer > money) ? answer - money : 0;
}