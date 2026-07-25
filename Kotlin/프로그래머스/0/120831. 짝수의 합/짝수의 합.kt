class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var new_n = if (n % 2 == 1) n-1 else n
        while (new_n > 0) {
            answer += new_n
            new_n -= 2
        }
        return answer
    }
}