import java.util.HashMap;

class Solution {
    public int solution(int left, int right) {
        int answer = 0;

        for(int i=left; i<=right; i++) answer += (isItOdd(i)) ? -i : i;

        return answer;
    }

    static boolean isItOdd(int num){
        HashMap<Integer,Integer> map = new HashMap<>();
        int dividing_num = 2;
        
        while(num>1){
            if(num%dividing_num==0) {
                map.put(dividing_num, map.getOrDefault(dividing_num,0)+1);
                num/=dividing_num;
            }
            else dividing_num++;
        }
        
        int factors = 1; //약수 개수
        for(int i : map.values()) factors=factors*(i+1);
        
        return factors % 2 == 1;
    }

}