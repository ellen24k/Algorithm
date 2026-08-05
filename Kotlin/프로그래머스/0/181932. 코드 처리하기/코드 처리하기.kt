class Solution {
    fun solution(code: String): String {
        val answer = mutableListOf<Char>()
        var mode = 0
        
        for ((index, char) in code.withIndex()) {
            if (char == '1') {
                mode = if (mode == 0) 1 else 0
            }
            else if (index % 2 == mode) {
                answer.add(char)
            }
        }
    return if (answer.isEmpty()) "EMPTY" else answer.joinToString(separator = "")
    }
}