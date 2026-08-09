class Solution {
    fun solution(array: IntArray): IntArray = intArrayOf(array.maxOf { it }, array.indexOf(array.maxOf { it }))
}