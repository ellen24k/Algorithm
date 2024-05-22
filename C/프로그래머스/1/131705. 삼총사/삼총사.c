#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int number[], size_t number_len) {
    int answer = 0;

    for (int student1 = 0; student1 < number_len - 2; student1++) {
        for (int student2 = student1+1; student2 < number_len - 1; student2++) {
            for (int student3 = student2+1; student3 < number_len; student3++) {
                if (number[student1] + number[student2] + number[student3] == 0) {
                    answer++;
                }
            }
        }
    }

    return answer;
}