#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int storey) {
    int answer = 0;
    int count;
    while (storey) {
        count = storey % 10;
        answer += (count > 5) ? 10 - count : count;
        
        if (count > 5 || (count == 5 && (storey % 100 > 50)))
            storey += 10 - count;
        storey/=10;
    }

    return answer;
}