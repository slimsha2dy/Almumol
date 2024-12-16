class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        val termMap = terms.associate { term ->
            val (t, m) = term.split(" ")
            t to m.toInt()
        }

        val todayInt = dayToInt(today)

        val result = privacies.mapIndexed { idx, privacy ->
            val (date, type) = privacy.split(" ")
            val added = addDay(date, termMap[type] ?: 0)
            if (todayInt >= dayToInt(added)) (idx + 1) else null
        }.filterNotNull()

        return result.toIntArray()
    }

    private fun dayToInt(date: String): Int {
        val (y, mo, d) = date.split(".").map(String::toInt)
        return y * 12 * 28 + mo * 28 + d
    }

    private fun addDay(date: String, addMonth: Int): String {
        val addDay = addMonth * 28
        var (y, mo, d) = date.split(".").map(String::toInt)

        d += addDay
        if (d > 28) {
            mo += d / 28
            d %= 28
        }
        if (mo > 12) {
            y += mo / 12
            mo %= 12
        }

        return "$y.$mo.$d"
    }
}