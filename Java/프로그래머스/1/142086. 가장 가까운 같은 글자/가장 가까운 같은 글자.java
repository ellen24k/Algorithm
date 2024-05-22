import java.util.HashMap;

class Solution {
    public int[] solution(String s) {
        HashMap<Character, Integer> ansMap = new HashMap<>();
        int[] answer = new int[s.length()];

        int index = 0;
        for(char c : s.toCharArray()){
            answer[index] = ansMap.containsKey(c) ? index-ansMap.get(c) : -1;
            ansMap.put(c,index); // 값 추가 or 인덱스 갱신
            index++;
        }

        return answer;
    }
}