import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int len = 1;
        while (arr.length > len) len *= 2;
        return Arrays.copyOf(arr,len);
    }
}