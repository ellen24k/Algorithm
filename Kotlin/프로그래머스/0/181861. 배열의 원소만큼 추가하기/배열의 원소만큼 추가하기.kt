class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        for (a in arr) {
            for (i in 1..a) {
                answer.add(a)
            }
        }
        return answer.toIntArray()
    }
}