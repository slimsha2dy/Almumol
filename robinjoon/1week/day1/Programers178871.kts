class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        val map = HashMap<String,Int>()
        var index: Int = 0
        for(player in players) {
            map.put(player, index++)
        }
        
        for(call in callings) {
            val i = map.get(call)!!
            val before = players[i-1]
            map.put(before, i)
            map.put(call, i-1)
            players[i-1] = call
            players[i] = before
        }
        return players
    }
}