#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, int k) {
    int string_length = strlen(my_string);
    char* answer = (char*)malloc(string_length*k + 1);

    int index = 0;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < strlen(my_string); j++) {
            answer[index] = my_string[j];
            index++;
        }
    }
    answer[index] = '\0';
    return answer;
}