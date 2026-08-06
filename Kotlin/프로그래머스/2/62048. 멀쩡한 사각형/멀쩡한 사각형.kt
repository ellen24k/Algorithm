import kotlin.math.ceil
import kotlin.math.floor

class Solution {
    fun solution(w: Int, h: Int): Long {
        var answer: Long = w.toLong() * h.toLong() 
        var line = { px: Int -> -(h.toDouble() / w.toDouble()) * px + h } 
        
        // 미세한 부동소수점 오차를 잡기 위한 보정값
        val eps = 1e-9 
        
        for (i in 0 until w) { 
            // eps를 더하거나 빼서 정수 경계면에서 생기는 오작동을 방지
            val y1 = line(i) - eps
            val y2 = line(i + 1) + eps
            
            val damagedBlocks = ceil(y1).toLong() - floor(y2).toLong()
            answer -= damagedBlocks
        } 
        return answer
    }
}