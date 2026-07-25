class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = IntArray(2)
        num_list.forEach {num -> 
            if (num % 2 == 0) answer[0]++
            else answer[1]++
        }
        return answer
    }
}