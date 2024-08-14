#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int* make_combination(int* nums, size_t nums_len, int* combination_len) {
    *combination_len = (nums_len * (nums_len-1) * (nums_len-2)) / 6;
    int* combination_num_list = (int*)malloc(sizeof(int) * (*combination_len));
    // printf("combi size: %d\n", *combination_len);
    
    for (int first = 0, index = 0; first < nums_len - 2; first++){
        for (int second = first + 1; second < nums_len - 1; second++) {
            for (int third = second + 1; third < nums_len; third++) {
                combination_num_list[index++] = nums[first] + nums[second] + nums[third];
                // printf("%d %d %d\n", first, second, third);
                // printf("%d\n", combination_num_list[index - 1]);
            }
        }
    }
    
    return combination_num_list;
}

int is_prime(int num) {
    for (int i = 2; i <= (int)sqrt(num) + 1; i++) {
        if (num % i == 0) {
            // printf("not prime: %d - > %d\n", num, i);        
            return 0;
        }
    }
    // printf("prime: %d\n", num);
    return 1;
}

int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int combination_list_size;
    int* combination_num_list = make_combination(nums, nums_len, &combination_list_size);
    
    for (int i = 0; i < combination_list_size; i++) {
        if (is_prime(combination_num_list[i])) answer++;
    }
    
    free(combination_num_list);
    return answer;
}