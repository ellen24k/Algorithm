class Solution {
    fun solution(n: Int, k: Int): Int = 12000*n + 2000*(maxOf(k - n/10, 0))
}