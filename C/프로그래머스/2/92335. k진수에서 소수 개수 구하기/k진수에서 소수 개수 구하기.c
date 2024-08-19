#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int is_prime(long num) {
    if (num <= 1) return 0;
    if (num == 2) return 1;
    for (int i = 2; i <= (int)sqrt(num); i++) {
        if (num % i == 0) {
            // printf("not prime: %d - > %d\n", num, i);        
            return 0;
        }
    }
    // printf("prime: %d\n", num);
    return 1;
}

int solution(int n, int k) {
    int answer = 0;
    int count = 1; 
    
    int temp = n;
    while (temp > 0) {
        temp /= k;
        count++;
    }
    
    char* converted_num_in_char_arr = (char*)calloc(count + 1,sizeof(char));
    for (int i = count - 1; i >= 0; i--) {
        converted_num_in_char_arr[i] = n%k + '0';
        n/=k;
    }
    // printf("%s\n", converted_num_in_char_arr);
    
    for (int i = 0, start_index = 0; i <= count; i++) {
        if (converted_num_in_char_arr[i] == '0' || i == count) {
            if (i > start_index) {
                char length = i - start_index;
                char sub_string[length + 1];
                memcpy(sub_string, &converted_num_in_char_arr[start_index],length);
                sub_string[length] = '\0';
            
                if (is_prime(atol(sub_string))) {
                    // printf("%d\n", atol(sub_string));
                    answer++;
                }
                start_index = i + 1;
            }
        }
        
    }
    free(converted_num_in_char_arr);
    return answer;
}