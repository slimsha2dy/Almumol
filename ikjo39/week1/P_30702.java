import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class P_30702 {

    static int[] dx = {-1, 0, 0, 1};
    static int[] dy = {0, -1, 1, 0};
    static boolean[][] visited;
    static Queue<int[]> queue;
    static char[][] A;
    static char[][] B;
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        A = new char[n][m];
        B = new char[n][m];
        visited = new boolean[n][m];
        queue = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            A[i] = br.readLine().toCharArray();
        }
        for (int i = 0; i < n; i++) {
            B[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    queue.offer(new int[]{i, j});
                    changeColor(i, j);
                }
            }
        }

        String result = getResult();
        bw.write(result + System.lineSeparator());
        bw.flush();
    }

    private static String getResult() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (A[i][j] != B[i][j] || !Character.isUpperCase(A[i][j])) {
                    return "NO";
                }
            }
        }
        return "YES";
    }

    private static void changeColor(int i, int j) {
        char before = A[i][j];
        A[i][j] = B[i][j];
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            for (int d = 0; d < dx.length; d++) {
                int newX = now[0] + dx[d];
                int newY = now[1] + dy[d];

                if (newX < 0 || newX >= n || newY < 0 || newY >= m) {
                    continue;
                }
                if (before != A[newX][newY]) {
                    continue;
                }
                if (!visited[newX][newY]) {
                    visited[newX][newY] = true;
                    A[newX][newY] = A[i][j];
                    queue.offer(new int[]{newX, newY});
                }
            }
        }
    }
}
