import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class P_1806 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int[] sum = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        sum[1] = arr[0];
        for (int i = 1; i < n; i++) {
            sum[i + 1] = arr[i] + sum[i];
        }

        int start = 0;
        int end = start + 1;
        int minLen = Integer.MAX_VALUE;
        while (end <= n) {
            int total = sum[end] - sum[start];
            if (total >= s && start <= end) {
                minLen = Math.min(minLen, end - start);
                start++;
            } else {
                end++;
            }
        }
        minLen = (minLen == Integer.MAX_VALUE) ? 0 : minLen;
        bw.write(minLen + System.lineSeparator());
        bw.flush();
    }
}
