#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

void to_binary(int num_of_1, char* binary_array) {
    memset(binary_array, '\0', strlen(binary_array)+1);
    int two_to_the_power_of_N = 262144; //max 2^18
    int i = 0;

    while (two_to_the_power_of_N > num_of_1) two_to_the_power_of_N /= 2;
    while (two_to_the_power_of_N >= 1) {
        if (num_of_1 >= two_to_the_power_of_N) {
            num_of_1 -= two_to_the_power_of_N;
            binary_array[i] = '1';
        }
        else binary_array[i] = '0';
        i++;
        two_to_the_power_of_N /= 2;      
    }
}

int* solution(const char* s) {
    int* answer = (int*)malloc(sizeof(int) * 2); //[이진 변환 횟수, 제거된 0의 개수]
    memset(answer, 0, sizeof(int) * 2);
    char* binary_array = (char*)malloc(strlen(s)+1);
    strcpy(binary_array, s);

    int num_of_0 = 0;
    while (strlen(binary_array) != 1) {
        int num_of_1 = 0;
        answer[0]++;
        for (int i = 0; i < strlen(binary_array); i++)
            (binary_array[i] == '1') ? num_of_1++ : num_of_0++;
        to_binary(num_of_1, binary_array);
    }
    answer[1] = num_of_0;
    free(binary_array);
    return answer;
}