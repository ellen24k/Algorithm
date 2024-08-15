#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// section_len은 배열 section의 길이입니다.
int solution(int n, int m, int section[], size_t section_len) {
    int answer = 0;
    
    for (int i = 0, section_range = 0; i < section_len; i++) {
        if (section[i] > section_range) {
            answer++;
            section_range = section[i] + m - 1;
        }        
    }
    
    return answer;
}