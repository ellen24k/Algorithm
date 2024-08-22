#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int data[2];
    int count;
    struct Node* next;
} Node;

void append(Node** head, int row, int col, int cnt) { //마지막 원소 뒤에 append
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data[0] = row;
    new_node->data[1] = col;
    new_node->count = cnt;
    new_node->next = NULL;
    
    if (*head == NULL){
        *head = new_node;
    } else {
        Node* cur_last_node = *head;
        while(cur_last_node->next != NULL) {
            cur_last_node = cur_last_node->next;
        }
        cur_last_node->next = new_node;
    }
}

void delete(Node** head, int* row, int* col, int* cnt) { // 첫 번째 원소 삭제 & 데이터 리턴
    if (*head != NULL) {
        Node* temp = (*head);
        *head = (*head)->next;
        
        *row = temp->data[0];
        *col = temp->data[1];
        *cnt = temp->count;
        
        free(temp);
    }
}

void free_all(Node** head){
    Node* cur_node = *head;
    Node* next_node;
    
    while(cur_node != NULL) {
        next_node = cur_node->next;
        free(cur_node);
        cur_node = next_node;
    }
}

int bfs(char** board, int start_row, int start_col, int goal_row, int goal_col, int board_row, int board_col) {
    int weight[4][2] = {{0,1},{0,-1},{-1,0},{1,0}};
    
    // 목표 지점에 도달할 수 있는가
    if (goal_row != 0 && goal_row != board_row - 1 && 
        goal_col != 0 && goal_col != board_col - 1){ 
        bool is_stoppable = false;
        for (int i = 0; i < 4; i++) {
            if (board[goal_row + weight[i][0]][goal_col + weight[i][1]] == 'D') {
                is_stoppable = true;
                break;
            }
        }
        if (!is_stoppable) return -1;
    }
    
    
    bool visited[board_row][board_col];
    memset(visited, false, sizeof(visited));
    
    Node* head = NULL;
    append(&head, start_row, start_col, 0);
    visited[start_row][start_col] = true;
    
    int cur_row, cur_col, count = 1;
    int max_count = board_col * board_row;
    while(head != NULL && count < max_count) {
        delete(&head, &cur_row, &cur_col, &count);    
        count++;
        
        for (int i = 0; i < 4; i++) { // 상하좌우로 가능한 만큼 이동
            int new_row = cur_row + weight[i][0];
            int new_col = cur_col + weight[i][1];
            
            while(true) {
                if (new_row >= 0 && new_row < board_row 
                    && 
                    new_col >= 0 && new_col < board_col
                    &&
                    board[new_row][new_col] != 'D'
                   ) {
                        new_row += weight[i][0];
                        new_col += weight[i][1];
                } else {
                    new_row -= weight[i][0];
                    new_col -= weight[i][1];
                    break;
                }
            }
            
            if (new_row == goal_row && new_col == goal_col) { // 목표 지점에 도달했는가
                free_all(&head);
                return count;
            }
            
            if (!visited[new_row][new_col]) { // 큐에 추가
                append(&head, new_row, new_col, count);
                visited[new_row][new_col] = true;
            }
        }
    }
    free_all(&head);
    return -1;
}

int solution(const char* board[], size_t board_row) {
    int board_col = strlen(board[0]);
    int start_row, start_col, goal_row, goal_col;
    
    for (int i = 0; i < board_row; i++) {
        for (int j = 0; j < board_col; j++) {
            if (board[i][j] == 'R') {
                start_row = i;
                start_col = j;
            } else if (board[i][j] == 'G') {
                goal_row = i;
                goal_col = j;
            }
        }
    }
        
    // for (int i = 0; i < board_row; i++) { //for check
        // printf("%s\n", board[i]);
    // }
    // printf("\n");
    
    // printf("start_r: %d start_c: %d goal_r: %d goal_c row: %d col %d\n", start_row, start_col, goal_row, goal_col, board_row, board_col);
    int answer = bfs((char**)board, start_row, start_col, goal_row, goal_col, board_row, board_col);
    
    return answer;
}