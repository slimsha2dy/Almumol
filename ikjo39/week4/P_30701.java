import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P_30701 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long d = Long.parseLong(st.nextToken());

        PriorityQueue<Integer> pq1 = new PriorityQueue<>();
        PriorityQueue<Integer> pq2 = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            if (a == 1) {
                pq1.offer(x);
            } else if (a == 2) {
                pq2.offer(x);
            }
        }

        int result = 0;
        while (!pq1.isEmpty()) {
            if (pq2.isEmpty() && d <= pq1.peek()) {
                break;
            }

            while (!pq1.isEmpty() && d > pq1.peek()) {
                d += pq1.poll();
                result++;
            }

            if (!pq2.isEmpty()) {
                d *= pq2.poll();
                result++;
            }
        }

        while (!pq2.isEmpty()) {
            pq2.poll();
            result++;
        }

        bw.write(result + System.lineSeparator());
        bw.flush();
    }
}
