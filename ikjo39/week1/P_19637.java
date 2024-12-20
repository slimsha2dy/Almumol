import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P_19637 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<String> names = new ArrayList<>();
        List<Integer> values = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int value = Integer.parseInt(st.nextToken());
            names.add(name);
            values.add(value);
        }

        for (int i = 0; i < m; i++) {
            int input = Integer.parseInt(br.readLine());

            int start = 0;
            int end = values.size() - 1;

            while (start < end) {
                int mid = start + (end - start) / 2;
                int midVal = values.get(mid);

                if (input < midVal) {
                    end = mid;
                } else if (input > midVal) {
                    start = mid + 1;
                } else {
                    end = mid;
                }
            }

            bw.write(names.get(start) + System.lineSeparator());
        }
        bw.flush();
    }
}
