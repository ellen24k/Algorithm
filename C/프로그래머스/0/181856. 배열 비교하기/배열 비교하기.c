#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr1_len은 배열 arr1의 길이입니다.
// arr2_len은 배열 arr2의 길이입니다.
int solution(int arr1[], size_t arr1_len, int arr2[], size_t arr2_len) {
    
    int sum1 = 0;
    int sum2 = 0;
    
    if (arr1_len == arr2_len) {
        
        for(int i = 0; i < arr1_len; i++) {
            sum1 += arr1[i];
        }
        for(int i = 0; i < arr2_len; i++) {
            sum2 += arr2[i];
        }
        
        if (sum1 == sum2) return 0;
        return (sum1 > sum2) ? 1 : -1;
    } else {
        return (arr1_len > arr2_len) ? 1 : -1;
    }
}