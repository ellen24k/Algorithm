//#define _CRT_SECURE_NO_WARNINGS   // strcpy 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
//#include <string.h>    // strcat 함수가 선언된 헤더 파일
#include <stdlib.h>

char* solution(const char* X, const char* Y) {
    
    unsigned long arrX[] = { 0,0,0,0,0,0,0,0,0,0 }; //{0,1,2,3,4,5,6,7,8,9}의 개수
    unsigned long arrY[] = { 0,0,0,0,0,0,0,0,0,0 };
    unsigned long arrAnswer[] = { 0,0,0,0,0,0,0,0,0,0 };
    

    char* answer = (char *)malloc(sizeof(char)* 3000001); //(char *)malloc 이랑 malloc 차이
//    strcpy(answer, "");

    while (*X) {
        arrX[X[0] - 48] += 1;
        *X++;
    }
    while (*Y) {
        arrY[Y[0] - 48] += 1;
        *Y++;
    }

    for (int i = 0; i < 10; i++) { //10번 반복 문제 없을 듯
        if (arrX[i] >= arrY[i]) {
            arrAnswer[i] = arrY[i];
        }
        else {
            arrAnswer[i] = arrX[i];
        }
    }

//    strcpy(answer, "");
    char index[2];
    char isException = 1;
    unsigned int tempIndex = 0;
    for (int i = 9; i >= 0; i--) {
        if (i == 0 && isException == 1) {
            if (arrAnswer[0] == 0) {
                answer = "-1";
            }
            else {
                answer = "0";
            }
            return answer;
        }
        else {
            while (arrAnswer[i] > 0) {
                switch (i) {
                case 0:
                    answer[tempIndex++] = 0x30;
                    break;
                case 1:
                    answer[tempIndex++] = 0x31;
                    break;
                case 2:
                    answer[tempIndex++] = 0x32;
                    break;
                case 3:
                    answer[tempIndex++] = 0x33;
                    break;
                case 4:
                    answer[tempIndex++] = 0x34;
                    break;
                case 5:
                    answer[tempIndex++] = 0x35;
                    break;
                case 6:
                    answer[tempIndex++] = 0x36;
                    break;
                case 7:
                    answer[tempIndex++] = 0x37;
                    break;
                case 8:
                    answer[tempIndex++] = 0x38;
                    break;
                case 9:
                    answer[tempIndex++] = 0x39;
                    break;
                default:-1;
                }

                arrAnswer[i]--;
                isException = 0;
            }
        }
    }
    answer[tempIndex] = 0x00;
    return answer;
}