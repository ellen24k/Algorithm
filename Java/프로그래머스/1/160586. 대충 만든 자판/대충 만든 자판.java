import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        HashMap<Character, Integer> keys = new HashMap<>();
        int[] answer = new int[targets.length];
        Arrays.fill(answer, 0);

        for(String keyString : keymap) {
            for(int i=0; i<keyString.length(); i++){
                char keyChar = keyString.charAt(i);

                if(keys.getOrDefault(keyChar,i+1) <= i) continue; //기존값이 더 작음
                else keys.put(keyChar,i);
            }
        }
        
        for(int i=0;i< targets.length;i++){
            String targetString  = targets[i];
            
            for(char targetChar : targetString.toCharArray()){
                answer[i] += keys.getOrDefault(targetChar,-answer[i]-2)+1; 
                if (answer[i] == -1) break;
            }
        }
        
        return answer;
    }
}