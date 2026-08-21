class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var reachedPeople = stages.size
        var failratePerStage = mutableListOf<Pair<Int, Double>>()
        
        for (i in 1..N) {
            val failedPeople = stages.count{it == i}
            val failRate = if (reachedPeople > 0) failedPeople.toDouble() / reachedPeople else 0.0
            reachedPeople -= failedPeople
            failratePerStage.add(Pair(i,failRate))
        }
        
        failratePerStage.sortWith(
            compareByDescending<Pair<Int,Double>> {it.second}
            .thenBy{it.first}
        )
        
        return failratePerStage.map {it.first}.toIntArray()
    }
}