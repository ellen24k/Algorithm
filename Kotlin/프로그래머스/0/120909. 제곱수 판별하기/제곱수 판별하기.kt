import kotlin.math.floor
import kotlin.math.sqrt

class Solution {
    fun solution(n: Int): Int = if (sqrt(n.toDouble()) == floor(sqrt(n.toDouble()))) 1 else 2

}