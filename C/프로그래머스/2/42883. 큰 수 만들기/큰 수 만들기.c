#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* number, int k) {
    int answer_size = strlen(number) - k + 1; 
    char* answer = (char*)malloc(answer_size);
    memset(answer, '\0', answer_size);
    answer[0] = number[0];

    int ans_index = 0;
    int compare_index = 1;

    while (k) {
        if (answer[ans_index] >= number[compare_index]) { 
            answer[ans_index + 1] = number[compare_index];
            ans_index++;
            compare_index++;
        }
        else { 
            if (k == 1 || ans_index == 0) { 
                answer[ans_index] = number[compare_index];
                compare_index++;
            }
            else { 
                answer[ans_index] = '\0';
                ans_index--;
            }
            k--;
        }
    }
    strcat(answer, &number[compare_index]);
    answer[answer_size-1] = '\0'; 
    return answer;
}