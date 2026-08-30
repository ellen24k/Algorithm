class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer = num_list.toMutableList()
        val (first, second) = num_list.takeLast(2)
        if (first < second) answer.add(second - first)
        else answer.add(second*2)
        return answer.toIntArray()
    }
}