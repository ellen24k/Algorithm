#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString) {
    char* answer = (char*)calloc(strlen(myString) + 1,sizeof(char));
    
    for(int i = 0; i < strlen(myString); i++) {
        switch(myString[i]) {
            case 'a':
            case 'A':
                answer[i] = 'A';
                break;
            case ' ':
                answer[i] = ' ';
                break;
            default: 
                answer[i] = (myString[i] < 'a') ? myString[i] + ('a' - 'A') : myString[i];
                break;
        }
    }
    
    return answer;
}