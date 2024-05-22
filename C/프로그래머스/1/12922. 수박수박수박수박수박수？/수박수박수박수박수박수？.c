#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n) {
    char* answer = (char*)malloc(n*3+1);
    
    for(int i=0; i<n; i++) {
        if(i%2) strncpy(&answer[i*3],"\ubc15\0",4); //박
        else strncpy(&answer[i*3],"\uc218\0",4); //수
    }
    return answer;
}