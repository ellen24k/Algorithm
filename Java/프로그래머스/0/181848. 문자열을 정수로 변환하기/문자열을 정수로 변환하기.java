class Solution {
    public int solution(String n_str) {
        int answer = 0;
        for(int i=0; i<n_str.length();i++){
            answer = answer*10 + (n_str.charAt(i)-'0');
        }
        return answer;
    }
}