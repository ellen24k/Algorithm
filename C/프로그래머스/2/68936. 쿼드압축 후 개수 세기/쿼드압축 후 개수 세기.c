#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void QuadTree(int**, int, int, int, int*);

int* solution(int** arr, size_t arr_rows, size_t arr_cols) {
    int* answer = (int*)calloc(2, sizeof(int));
    
    QuadTree(arr, 0, 0, arr_rows, answer);
    
    return answer;
}

void QuadTree(int** arr, int row, int col, int length, int* answer) {
    int first_val = arr[row][col]; // 해당 쿼드의 기준값이 되는 첫 번째 값
    // printf("fir: %d, r: %d, c: %d, len: %d\n", first_val, row, col, length);

    for (int i = row; i < row + length; i++) {        
        for (int j = col; j < col + length; j++) {
            if (arr[i][j] != first_val) { // 기준값과 다른 값이 있다면 새로 영역을 나누어야 함
                int half_len = length / 2;
                
                QuadTree(arr, row, col, half_len, answer); // upper left
                QuadTree(arr, row, col + half_len, half_len, answer); // upper right
                QuadTree(arr, row + half_len, col, half_len, answer); // lower left
                QuadTree(arr, row + half_len, col + half_len, half_len, answer); // lower right
                // printf("\n");
                return;
            }
        }      
        
    }
    // printf("r: %d c: %d answer++  %d\n\n", row, col, first_val);
    answer[first_val]++; // 압축 완료 상태이므로 first value의 사용 횟수 추가
}
