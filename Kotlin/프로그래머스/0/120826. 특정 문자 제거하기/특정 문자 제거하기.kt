class Solution {
    fun solution(my_string: String, letter: String): String {
        val char_letter = letter[0]
        
        return my_string.filterNot { it == char_letter }
    }
}