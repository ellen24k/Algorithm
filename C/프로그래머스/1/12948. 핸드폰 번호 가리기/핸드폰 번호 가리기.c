#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


char* solution(const char* phone_number) {
    int phone_num_len = strlen(phone_number);
    char* answer = (char*)malloc(phone_num_len + 1);
    memset(answer, '\0', phone_num_len + 1);
    
    strncpy(answer, phone_number, phone_num_len);
    strncpy(answer, "****************", phone_num_len - 4);
    
    return answer;
}