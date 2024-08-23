#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int get_type_index(char type) {
    int answer = -1;
    switch(type) {
        case 'R':
            answer = 0; break;
        case 'T':
            answer = 1; break;
        case 'C':
            answer = 2; break;
        case 'F':
            answer = 3; break;
        case 'J':
            answer = 4; break;
        case 'M':
            answer = 5; break;
        case 'A':
            answer = 6; break;
        case 'N':
            answer = 7; break;
    }
    return answer;
}

char* solution(const char* survey[], size_t survey_len, int choices[], size_t choices_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int type_score[] = {0,0,0,0,0,0,0,0}; // R T C F J M A N
    
    for (int i = 0; i < choices_len; i++) {
        // printf("choice: %d\n", choices[i]);
        switch(choices[i]) {
            case 1:
                type_score[get_type_index(survey[i][0])] += 3;
                break;
            case 2:
                type_score[get_type_index(survey[i][0])] += 2;
                break;
            case 3:
                type_score[get_type_index(survey[i][0])] += 1;
                break;
            case 5:
                type_score[get_type_index(survey[i][1])] += 1;
                break;
            case 6:
                type_score[get_type_index(survey[i][1])] += 2;
                break;
            case 7:
                type_score[get_type_index(survey[i][1])] += 3;
                break;
        }
    }
    
    char* answer = (char*)calloc(5, sizeof(char));
    char* types = "RTCFJMAN";
    for (int i = 0; i < 4; i++) {
        // printf("%d vs %d\n", type_score[i*2], type_score[i*2 + 1]);
        answer[i] = (type_score[i*2] - type_score[i*2+ 1] >= 0) ? types[i*2] : types[i*2 + 1];
    }
    
    return answer;
}