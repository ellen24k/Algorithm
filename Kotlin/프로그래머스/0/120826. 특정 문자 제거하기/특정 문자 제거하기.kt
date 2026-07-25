class Solution {
    fun solution(my_string: String, letter: String): String {
        val char_letter = letter[0]
        
        return buildString(my_string.length) {
            my_string.forEach { my_char ->
                if (my_char != char_letter) append(my_char)
            }
        }
    }
}