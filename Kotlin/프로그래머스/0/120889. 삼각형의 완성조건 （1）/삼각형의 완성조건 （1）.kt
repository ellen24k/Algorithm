class Solution {
    fun solution(sides: IntArray): Int {
        sides.sortDescending()
        // println(sides.contentToString()) 
        return if (sides[0] < sides[1] + sides[2]) 1 else 2
    }
}