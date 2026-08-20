import kotlin.math.max

class Solution {
    fun solution(a: Int, b: Int): Int = max((a.toString() + b.toString()).toInt(), 2*a*b)
}