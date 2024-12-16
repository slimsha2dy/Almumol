class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        val map = clothes.groupBy { it[1] }.mapValues { it.value.size }.values

        var result = 1
        map.forEach { result *= it + 1 }
        return result - 1
    }
}