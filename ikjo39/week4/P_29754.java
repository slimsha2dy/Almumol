import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    private static class Broadcast {
        long totalTime;

        public Broadcast(int startH, int startM, int endH, int endM) {
            this.totalTime = (endH * 60L + endM) - (startH * 60L + startM);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int standard = (m - 1) / 7 + 1;

        Map<String, Map<Integer, List<Broadcast>>> youtubers = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            youtubers.putIfAbsent(name, new HashMap<>());

            int day = Integer.parseInt(st.nextToken());
            int week = (day - 1) / 7;
            Map<Integer, List<Broadcast>> weekBroadcasts = youtubers.get(name);
            weekBroadcasts.putIfAbsent(week, new ArrayList<>());

            String startTime = st.nextToken();
            String[] startSplit = startTime.split(":");
            int startH = Integer.parseInt(startSplit[0]);
            int startM = Integer.parseInt(startSplit[1]);
            String endTime = st.nextToken();
            String[] endSplit = endTime.split(":");
            int endH = Integer.parseInt(endSplit[0]);
            int endM = Integer.parseInt(endSplit[1]);
            Broadcast broadcast = new Broadcast(startH, startM, endH, endM);
            weekBroadcasts.get(week).add(broadcast);
        }

        List<String> names = youtubers.entrySet().stream()
                .filter(entry -> {
                    Map<Integer, List<Broadcast>> weeklyBroadcasts = entry.getValue();
                    int size = weeklyBroadcasts.size();
                    return size == standard;
                })
                .filter(entry -> {
                    Map<Integer, List<Broadcast>> weekBroadCasts = entry.getValue();
                    for (int key : weekBroadCasts.keySet()) {
                        List<Broadcast> broadcasts = weekBroadCasts.get(key);
                        long totalTime = calculateTotalHours(broadcasts);
                        if (broadcasts.size() < 5 || totalTime < 60) {
                            return false;
                        }
                    }
                    return true;
                })
                .map(Entry::getKey)
                .sorted()
                .collect(Collectors.toList());

        if (names.isEmpty()) {
            names.add("-1");
        }

        for (String name : names) {
            bw.write(name + System.lineSeparator());
        }

        bw.flush();
    }

    private static long calculateTotalHours(List<Broadcast> broadcasts) {
        long totalTime = broadcasts.stream()
                .map(broadcast -> broadcast.totalTime)
                .mapToLong(Long::longValue)
                .sum();
        totalTime /= 60;
        return totalTime;
    }
}
