class Solution {
    fun solution(num_list: IntArray): IntArray {
        return num_list.sortedArray().copyOfRange(0,5)
    }
}