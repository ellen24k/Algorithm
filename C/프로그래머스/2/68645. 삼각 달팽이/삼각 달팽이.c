#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)calloc(n*(n+1)/2, sizeof(int));
    int index = 0; int num = 1; int gap = 0;
    
    while ( n > 0 ) {
        for (int i = 0; i < n; i++){ // 왼쪽 아래로 이동
            index += gap++;
            answer[index] = num++;
            // printf("step1: index: %d, gap: %d, %d\n", index, gap, answer[index]);
        }
        // printf("\n");
    	if (--n == 0) break;
        
    	for (int i = 0; i < n; i++) { // 가로 이동
            answer[++index] = num++;
            // printf("step2: index: %d, gap: %d, %d\n", index, gap, answer[index]);
        }
        // printf("\n");
    	if (--n == 0) break;
        
    	for (int i = 0; i < n; i++) { // 왼쪽 위로 이동
            index -= gap--;
            answer[index] = num++;
            // printf("step3: index: %d, gap: %d, %d\n", index, gap, answer[index]);
        }
        // printf("\n");
        n--;    
    }
    
    return answer;
}