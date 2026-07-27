class Solution {
    fun solution(n: Int) = (1..n).count { n % it == 0 }
}