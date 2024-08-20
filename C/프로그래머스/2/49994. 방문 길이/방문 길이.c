#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* dirs) {
    int answer = 0;
    int dirs_len = strlen(dirs);
    int  (*coordinates)[4] = (int (*)[4])calloc(dirs_len + 1, sizeof(int[4])); // (0,0) -> (1,0) 이동을 (0,0,1,0)으로 표현
    
    int new_coordinate[2] = {0,0}; // x,y
    int prev_coordinate[2] = {0,0};
    for (int i = 0; i < dirs_len; i++) {
        memcpy(prev_coordinate, new_coordinate, 2*sizeof(int));
        bool visited = false; // 해당 길을 지나간 적이 있는가 확인용
        
		switch(dirs[i]) {
            case 'U':
                if (new_coordinate[1] < 5) new_coordinate[1]++;
                else visited = true; // 좌표가 변하지 않은 것은 이동하지 않은 것
                break;
            case 'D':
                if (new_coordinate[1] > -5) new_coordinate[1]--;
                else visited = true;
                break;
            case 'R':
                if (new_coordinate[0] < 5) new_coordinate[0]++;
                else visited = true;
                break;
            case 'L':
                if (new_coordinate[0] > -5) new_coordinate[0]--;
                else visited = true;
                break;
        }
        
        for (int j = 0; j <= i; j++) {
            // 길을 같은 방향으로 지나간 적이 있는가
            if (prev_coordinate[0] == coordinates[j][0] && prev_coordinate[1] == coordinates[j][1]) {
                if (new_coordinate[0] == coordinates[j][2] && new_coordinate[1] == coordinates[j][3]) {
                    visited = true;
                }
            }
            // 길을 반대 방향으로 지나간 적이 있는가
            if (prev_coordinate[0] == coordinates[j][2] && prev_coordinate[1] == coordinates[j][3]) {
                if (new_coordinate[0] == coordinates[j][0] && new_coordinate[1] == coordinates[j][1]) {
                    visited = true;
                }
            }
        }
        
        if (!visited) {
            coordinates[answer][0] = prev_coordinate[0];
            coordinates[answer][1] = prev_coordinate[1];
            coordinates[answer][2] = new_coordinate[0];
            coordinates[answer][3] = new_coordinate[1];
            answer++;
        }
        // printf("[%d, %d, %d, %d] ", coordinates[answer-1][0], coordinates[answer-1][1], coordinates[answer-1][2], coordinates[answer-1][3]);
        // printf("%d \n", answer);
    }
    
    free(coordinates);
    return answer;
}

/* 시도 1: 방향을 고려하지 않고 좌표만 고려함
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* dirs) {
    int answer = 0;
    int dirs_len = strlen(dirs);
    int  (*coordinates)[2] = (int (*)[2])calloc(dirs_len + 1, sizeof(int[2]));
    
    int new_coordinate[2] = {0,0}; // x,y
    for (int i = 0; i < dirs_len; i++) {
		switch(dirs[i]) {
            case 'U':
                if (new_coordinate[1] < 5) new_coordinate[1]++;
                break;
            case 'D':
                if (new_coordinate[1] > -5) new_coordinate[1]--;
                break;
            case 'R':
                if (new_coordinate[0] < 5) new_coordinate[0]++;
                break;
            case 'L':
                if (new_coordinate[0] > -5) new_coordinate[0]--;
                break;
        }
        bool visited = false;
        for (int j = 0; j <= i; j++) {
            if (coordinates[j][0] == new_coordinate[0] && coordinates[j][1] == new_coordinate[1]) {
               visited = true; 
            }
        }
        if (!visited) {
            answer++;
            coordinates[i + 1][0] = new_coordinate[0];
            coordinates[i + 1][1] = new_coordinate[1];
        }
        printf("[%d,%d] %d\n", coordinates[i + 1][0], coordinates[i + 1][1], answer);
    }
    
    free(coordinates);
    return answer;
}
*/