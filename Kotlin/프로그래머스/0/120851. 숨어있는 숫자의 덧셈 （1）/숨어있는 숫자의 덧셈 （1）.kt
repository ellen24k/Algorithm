class Solution {
    fun solution(my_string: String): Int = 
        my_string.filter(Char::isDigit)
        .sumOf(Char::digitToInt)
}