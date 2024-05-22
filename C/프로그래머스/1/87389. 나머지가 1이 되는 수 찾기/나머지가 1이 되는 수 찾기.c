int solution(int n) {
    int answer = 0;

    if (n % 2 == 1) { // 홀수
        answer = 2;
    } else {
        answer = 3;
        while (n % answer != 1) answer += 2;
    }
    return answer;
}