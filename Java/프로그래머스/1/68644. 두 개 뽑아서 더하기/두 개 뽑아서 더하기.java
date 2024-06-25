import java.util.Arrays;
import java.util.TreeSet;

class Solution {
    public int[] solution(int[] numbers) {
        Arrays.sort(numbers);
        TreeSet<Integer> setNumbers = new TreeSet<>();
        
        for(int i = 0; i < numbers.length-1; i++) {
            for(int j = i+1; j < numbers.length; j++) {
                setNumbers.add(numbers[i]+numbers[j]);
            }
        }
        
        return setNumbers.stream().mapToInt(Integer::intValue).toArray();
    }
}