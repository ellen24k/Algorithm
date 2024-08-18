#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* my_string, const char* is_suffix) {
    if (strlen(my_string) < strlen(is_suffix)) return 0;
    for (int i = strlen(my_string) - strlen(is_suffix), j = 0; i < strlen(my_string); i++, j++) {
        if (my_string[i] != is_suffix[j]) return 0;
    }    
    
    return 1;
}