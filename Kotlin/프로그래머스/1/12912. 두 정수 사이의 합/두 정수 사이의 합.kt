class Solution {
    fun solution(a: Int, b: Int): Long {
        var answer: Long = 0
        
        when {
            (a < b) -> for (i in a..b) answer += i
            (a > b) -> for (i in b..a) answer += i
            else -> return a.toLong()
        }
        
        return answer
    }
}