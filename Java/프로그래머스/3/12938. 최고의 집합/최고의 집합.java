class Solution {
    public int[] solution(int n, int s) {
            if(n>s) return new int[]{-1};

            int index = 0;
            int[] answer = new int[n];
            while(n>0){
                answer[index] = s/n;
                index++;
                s-=s/n;
                n--;
            }

            return answer;
    }
}