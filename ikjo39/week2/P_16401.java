import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P_16401 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int jokaCount = Integer.parseInt(st.nextToken());
        int snackCount = Integer.parseInt(st.nextToken());

        int[] snacks = new int[snackCount];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < snackCount; i++) {
            snacks[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(snacks);
        int left = 1;
        int right = snacks[snackCount - 1];
        int result = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            for (int snack : snacks) {
                count += snack / mid;
            }

            if (count >= jokaCount) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        bw.write(result + System.lineSeparator());
        bw.flush();
    }
}
