class Solution {
    public int solution(int[] ingredient) {
        int [] burgerSet = new int[ingredient.length+1];
        int answer = 0;
        int burgerSetIdx = 0;

        for(int i : ingredient) {
            if(i==burgerSet[burgerSetIdx]+1) burgerSet[(burgerSetIdx++) + 1] = i;
            
            else if(burgerSet[burgerSetIdx] == 3 && i ==1){
                answer++;
                burgerSetIdx -= 3;
            }
            
            else burgerSet[(burgerSetIdx++) + 1] = (i == 1) ? 1 : 0;
        }
        return answer;
    }
}