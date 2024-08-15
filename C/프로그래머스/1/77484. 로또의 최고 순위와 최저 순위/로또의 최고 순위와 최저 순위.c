#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    int* answer = (int*)malloc(2*sizeof(int));
    int same_num_count = 0;
    int zero_count = 0;
    
    for (int i = 0; i < 6; i++) {
        if (lottos[i] != 0) {
            for (int j = 0; j < 6; j++) {
                if (lottos[i] == win_nums[j]) same_num_count++;
            }
        } else zero_count++;
    }
    
    answer[0] = (same_num_count == 0 && zero_count == 0) ? 6 : 7 - same_num_count - zero_count;
    answer[1] = (same_num_count == 0) ? 6 : 7 - same_num_count;
    
    return answer;
}
