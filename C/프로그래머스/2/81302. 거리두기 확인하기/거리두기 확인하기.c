#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int get_manhatten_distance(int r1, int c1, int r2, int c2) {
    return abs(r1-r2) + abs(c1-c2);
}

int check_distancing(char** place) {
    int p_coordinates[25][2] = {0,};
    int p_count = 0;
    
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (place[i][j] == 'P') {
                p_coordinates[p_count][0] = i;
                p_coordinates[p_count][1] = j;
                p_count++;
            }
        }
    }
    // printf("%d\n", p_count);
    
    for (int i = 0; i < p_count - 1; i++) {
        for (int j = i + 1; j < p_count; j++) {
            // printf("coordinates: (%d, %d) (%d, %d) \n", p_coordinates[i][0], p_coordinates[i][1], p_coordinates[j][0], p_coordinates[j][1]);
            if (get_manhatten_distance(p_coordinates[i][0], p_coordinates[i][1], p_coordinates[j][0], p_coordinates[j][1]) <= 2) {
                bool has_partition = false;
                // printf("distance <= 2\n");
                
                if (p_coordinates[i][0] == p_coordinates[j][0]) { // 같은 행
                    // printf("행\n");
                    if (p_coordinates[i][1] + 1 < 5 && place[p_coordinates[i][0]][p_coordinates[i][1] + 1] == 'X') has_partition = true;
                } else if (p_coordinates[i][1] == p_coordinates[j][1]) { // 같은 열
                    // printf("열\n");
                    if (p_coordinates[i][0] + 1 < 5 && place[p_coordinates[i][0] + 1][p_coordinates[i][1]] == 'X') has_partition = true;
                } else { // 대각선
                    // printf("대각선\n");
                    if (place[p_coordinates[j][0]][p_coordinates[i][1]] == 'X' && place[p_coordinates[i][0]][p_coordinates[j][1]] == 'X') has_partition = true;
                }
                
                if (!has_partition) {
                    // printf("\n 0\n");
                    return 0;
                }
            }
        }
    }
    // printf("\n 1\n");
    return 1;
}

int* solution(const char*** places, size_t places_rows, size_t places_cols) {
    int* answer = (int*)calloc(5,sizeof(int));
    
    for (int i = 0; i < 5; i++) {
        // for (int j = 0; j < 5; j++) printf("%s\n", places[i][j]);        
        answer[i] = check_distancing((char**)places[i]);
    }
    
    return answer;
}