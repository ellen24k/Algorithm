class Solution {
    public String solution(String my_string, int n) {        
        StringBuilder answer = new StringBuilder();
        String[] m_str_split = my_string.split("");
        
        for(int i=0; i<my_string.length(); i++){
            answer.append(m_str_split[i].repeat(n));
        }
        
        return answer.toString();
    }
}