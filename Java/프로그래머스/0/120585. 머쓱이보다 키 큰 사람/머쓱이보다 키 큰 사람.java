import java.util.Arrays;

class Solution {
    public int solution(int[] array, int height) {
        Arrays.sort(array);
        int answer = 0;
        for(int a : array){
            if(a<=height) answer++;
            else break;
        }
        return array.length - answer;
    }
}