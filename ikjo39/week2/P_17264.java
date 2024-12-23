import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class P_17264 {

    static int win;
    static int lose;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int gameCount = Integer.parseInt(st.nextToken());
        int playerCount = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        win = Integer.parseInt(st.nextToken());
        lose = Integer.parseInt(st.nextToken());
        int goal = Integer.parseInt(st.nextToken());

        Map<String, String> infos = new HashMap<>();

        for (int i = 0; i < playerCount; i++) {
            st = new StringTokenizer(br.readLine());
            infos.put(st.nextToken(), st.nextToken());
        }

        String result = "I AM IRONMAN!!";
        int point = 0;
        for (int i = 0; i < gameCount; i++) {
            String duo = br.readLine();
            point = Math.max(0, point + getPoint(infos, duo));
            if (point >= goal) {
                result = "I AM NOT IRONMAN!!";
                break;
            }
        }
        bw.write(result + System.lineSeparator());
        bw.flush();
    }

    private static int getPoint(Map<String, String> infos, String duo) {
        if (infos.containsKey(duo) && "W".equals( infos.get(duo))) {
            return win;
        }
        return -lose;
    }
}
