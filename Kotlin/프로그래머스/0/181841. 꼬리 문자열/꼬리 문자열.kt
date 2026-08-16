class Solution {
    fun solution(str_list: Array<String>, ex: String): String = str_list.filterNot { ex in it }.joinToString("")
}