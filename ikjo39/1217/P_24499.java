import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class P_24499 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] pies = new int[n * 2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            pies[i] = pies[i + n] = Integer.parseInt(st.nextToken());
        }

        int cur = 0;
        for (int i = 0; i < k; i++) {
            cur += pies[i];
        }

        int maxSum = cur;

        for (int i = 1; i < n; i++) {
            cur = cur - pies[i - 1] + pies[i + k - 1];
            maxSum = Math.max(maxSum, cur);
        }
        bw.write(maxSum + System.lineSeparator());
        bw.flush();
    }
}
