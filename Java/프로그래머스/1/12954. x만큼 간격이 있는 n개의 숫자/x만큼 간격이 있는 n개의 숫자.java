import java.util.Arrays;

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        Arrays.setAll(answer, i -> (long)x*(i+1));
        return answer;
    }
}