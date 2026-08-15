class Solution {
    fun solution(price: Int) = 
        if(price >= 500000) (price * 0.8).toInt()
        else if (price >= 300000) (price * 0.9).toInt()
        else if (price >= 100000) (price * 0.95).toInt()
        else price
}