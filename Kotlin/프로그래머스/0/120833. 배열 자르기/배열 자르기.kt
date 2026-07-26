class Solution {
    fun solution(numbers: IntArray, num1: Int, num2: Int): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in num1..num2) answer = answer.plus(numbers[i])
        return answer
    }
}