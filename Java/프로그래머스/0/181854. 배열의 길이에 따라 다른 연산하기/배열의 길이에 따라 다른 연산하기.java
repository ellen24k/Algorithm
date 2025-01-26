import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = Arrays.copyOf(arr,arr.length);
        for (int i = (arr.length+1)%2; i < arr.length; i+=2) answer[i] += n;
        return answer;
    }
}