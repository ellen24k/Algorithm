class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0,0}; 
        int index = words.length;
                
        Loop : 
        for (int i = 0; i < words.length; i++){
            if( words[i].length() == 1 ) { // 한 글자 체크
                index = i;
                break;
            }
            for(int j = 0; j < i; j++){ // 겹치는 단어 체크
                if(words[i].equals(words[j])){ 
                    index = i;
                    break Loop;
                }
            }
        }
        
        for (int i = 0; i < words.length - 2; i++) { //끝 -> 시작 연결 체크
            if (words[i].charAt(words[i].length()-1) != 
                words[i+1].charAt(0)) {
                if (i+1 < index) index = i+1;
                break;
            }
        }
        
        if (index != words.length){
            switch ((index+1)%n) {
                case 0 :
                    answer[0] = n; 
                    answer[1] = (index + 1)/n;
                    break;
                default :
                    answer[0] = (index+1)%n; 
                    answer[1] = (index + 1)/n + 1;
                    break;
            }
        }
        return answer;
    }
}