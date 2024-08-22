#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int min(int i1, int i2) {
    return (i1 > i2) ? i2 : i1;
}

int max(int i1, int i2) {
    return (i1 > i2) ? i1 : i2;
}


// wallpaper_row은 배열 wallpaper의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* wallpaper[], size_t wallpaper_row) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(4*sizeof(int));
    int wallpaper_col = strlen(wallpaper[0]);
    int lux = wallpaper_row, luy = wallpaper_col, rdx = 0, rdy = 0;
    // printf("wall len: %d, strlen: %d\n", wallpapen_row, wallpaper_col);
    for (int row = 0; row < wallpaper_row; row++) {
        for (int col = 0; col < wallpaper_col; col++) {
            if (wallpaper[row][col] == '#') {
                lux = min(lux, row);
                luy = min(luy, col);
                rdx = max(rdx, row + 1);
                rdy = max(rdy, col + 1);
            }
        }
    }
    
    answer[0] = lux;
    answer[1] = luy;
    answer[2] = rdx;
    answer[3] = rdy;
    
    return answer;
}