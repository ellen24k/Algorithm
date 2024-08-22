#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// order_len은 배열 order의 길이입니다.
int solution(int order[], size_t order_len) {
    int* stack = (int*)calloc(order_len, sizeof(int)); 
    int stack_cnt = -1; // 원소가 존재하는 마지막 인덱스
    
    int answer = 0;
    int box_num = 1; // 컨테이너 벨트에 순서대로 놓인 상자의 번호
    while(box_num <= order_len || (stack_cnt >= 0 && stack[stack_cnt] == order[answer])) {
        // printf("B: box_num %d order %d stack count %d stack %d\n", box_num, order[answer], stack_cnt, stack[stack_cnt]);
        if (order[answer] == box_num) {
            answer++;
            box_num++;
        } else if (stack_cnt != -1 && order[answer] == stack[stack_cnt]) {
            answer++;
            stack[stack_cnt--] = 0;
        }else {
            stack[++stack_cnt] = box_num++;
        }
        // printf("A: box_num %d order %d stack count %d stack %d\n\n", box_num, order[answer], stack_cnt, stack[stack_cnt]);
    }
    free(stack);
    return answer;
}