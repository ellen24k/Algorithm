#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sizes_rows는 2차원 배열 sizes의 행 길이, sizes_cols는 2차원 배열 sizes의 열 길이입니다.
int solution(int** sizes, size_t sizes_rows, size_t sizes_cols) {
    int max_w=0;
    int max_h=0;
    int temp = 0;
    
    for(int i=0; i<sizes_rows; i++) { //가로길이가 길게 재정렬
        if (sizes[i][0] <= sizes[i][1]) {
            temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
    }
    
    for (int i=0; i < sizes_rows; i++) {//최대 가로,세로 길이 구하기
        max_w = (max_w >= sizes[i][0]) ? max_w : sizes[i][0];
        max_h = (max_h >= sizes[i][1]) ? max_h : sizes[i][1];
    }
    
    return max_w*max_h;
}