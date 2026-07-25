class Solution {
    fun solution(numbers: IntArray): Double = if (numbers.size > 0) numbers.sum().toDouble() / numbers.size else 0.toDouble()
}