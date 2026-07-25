class Solution {
    fun solution(my_string: String, n: Int): String =
        buildString(my_string.length*n) {
            for (my_char in my_string) repeat(n) {append(my_char)}
        }
}