import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P_27376 {

    static class Blinker {
        int posX;
        int turnT;
        int firstS;

        public Blinker(int x, int t, int s) {
            this.posX = x;
            this.turnT = t;
            this.firstS = s;
        }

        public long getGreenTime(long time) {
            long firstGreen = time - firstS;
            if (firstGreen < 0) {
                return firstS - time;
            }
            long state = (firstGreen / turnT) % 2;
            return state * (turnT - firstGreen % turnT);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        PriorityQueue<Blinker> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.posX));
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            pq.offer(new Blinker(x, t, s));
        }

        long time = 0;
        long pos = 0;

        while (!pq.isEmpty()) {
            int nextPos = pq.peek().posX;
            time += nextPos - pos;
            pos = nextPos;
            Blinker now = pq.poll();
            time += now.getGreenTime(time);
        }

        if (pos < n) {
            time += n - pos;
        }

        bw.write(time + System.lineSeparator());
        bw.flush();
    }
}
