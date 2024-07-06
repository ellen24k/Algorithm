#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string) {
    char* answer = calloc(strlen(my_string), sizeof(char));
    
    for(int i = 0, j = 0; i<strlen(my_string); i++) {
        switch(my_string[i]) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                break;
            default:
                answer[j++] = my_string[i];
                break;
        }
    }
    return answer;
}