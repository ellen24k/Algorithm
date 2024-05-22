import java.util.HashMap;

class Solution {
    public static int solution(int[] arr) {
        HashMap<Integer,Integer> totalMap = new HashMap<>();
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int num : arr) { //배열의 원소마다
            int dividingNum = 2;
            while(num>1){ //소인수분해
                if(num%dividingNum==0) {
                    map.put(dividingNum, map.getOrDefault(dividingNum,0)+1);//시간초과 나오면 배열 하나 더 만들기
                    num/=dividingNum;
                }
                else dividingNum++;
            }

            for(int key : map.keySet()) //totalMap에 기존 값 중 가장 큰 인수,지수 저장
                if(totalMap.getOrDefault(key,0) < map.get(key)) totalMap.put(key,map.get(key));
            
            map.clear();
        }
        
        int answer = 1;
        for(int key : totalMap.keySet()) { //전부 곱해서 최소공배수
            answer *= (int) Math.pow(key, totalMap.get(key));
        }


        return answer;
    }
}