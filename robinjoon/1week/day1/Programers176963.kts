class Solution {
    fun solution(name: Array<String>, yearning: IntArray, photo: Array<Array<String>>): IntArray {
        var index: Int = 0
        val map = name.toList().map {
            it to index++
        }.toMap()
        return photo.toList().map { photoArray ->
            photoArray.map {
                map[it]
            }.filterNotNull().sumOf { yearning[it] }
        }.toIntArray()
    }
}