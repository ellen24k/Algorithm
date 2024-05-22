import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>(List.of(arr[0]));
        
        for(int i = 1; i < arr.length;i++){
            if(arr[i] != answer.get(answer.size()-1)) answer.add(arr[i]);
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}