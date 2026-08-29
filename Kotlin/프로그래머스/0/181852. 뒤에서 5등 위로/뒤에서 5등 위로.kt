class Solution {
    fun solution(num_list: IntArray): IntArray = num_list.sorted().takeLast(num_list.size - 5).toIntArray()
}