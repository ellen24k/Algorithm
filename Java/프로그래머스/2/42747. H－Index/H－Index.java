import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public static int solution(int[] citations) {
        Arrays.sort(citations); // 오름차순 정렬
        
        List<Integer> citationsList = new ArrayList<>(); //정렬된 값 리스트에 추가
        for(int i : citations){
            citationsList.add(i);
        }

        int hIndex = citations[citations.length/2]; //hIndex의 최댓값은 배열의 중간
        int index = citationsList.indexOf(hIndex); //hIndex와 같은 값을 가진 첫 인덱스값

        while(hIndex > citations.length - index){
            hIndex--;
            if ( citationsList.contains(hIndex)) index = citationsList.indexOf(hIndex);
        }

        return hIndex;
    }
}