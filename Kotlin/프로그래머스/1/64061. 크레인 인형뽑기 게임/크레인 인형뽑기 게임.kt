class Solution {
    lateinit var globalBoard: Array<IntArray>
    
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        globalBoard = board
        // 뽑은 인형을 넣는 바구니
        val basket = mutableListOf<Int>()
        
        for (move in moves) {
            val doll = get_poppable_doll_of_col(move - 1)
            
            // 뽑은 인형이 없는 경우(빈 줄) 무시
            if (doll == 0) continue
        
            // 바구니가 비어있지 않고 
            if (basket.isNotEmpty() && basket.last() == doll) { // 맨 위 인형과 일치하는 경우
                basket.removeLast() // 기존 인형 제거
                answer += 2 // 인형 2개가 사라지므로 +2
            } 
            else { // 맨 위 인형과 일치하지 않는 경우
                basket.add(doll)
            }
        }
        
        return answer
    }
    
    // 세로줄 가장 위의 인형 구하기
    fun get_poppable_doll_of_col(col: Int): Int {
        for (row in globalBoard.indices) {
            if (globalBoard[row][col] != 0) {
                val top_doll = globalBoard[row][col]
                globalBoard[row][col] = 0
                return top_doll
            }
        }
        return 0 // 해당 줄이 모두 비어있으면 0 반환
    }
}