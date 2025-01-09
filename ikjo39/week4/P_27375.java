import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P_27375 {

    static int result = 0;

    static class Subject {
        int dayOfWeek;
        int start;
        int end;
        int point;

        public Subject(int dayOfWeek, int start, int end) {
            this.dayOfWeek = dayOfWeek;
            this.start = start;
            this.end = end;
            this.point = end - start + 1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<Subject> subjects = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int dayOfWeek = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            Subject subject = new Subject(dayOfWeek, start, end);
            if (dayOfWeek == 5 || subject.point > k) continue;
            subjects.add(subject);
        }

        backTracking(k, 0, 0, subjects, new boolean[5][11]);
        bw.write(result + System.lineSeparator());
        bw.flush();
    }

    static void backTracking(int k, int cnt, int index, List<Subject> subjects, boolean[][] visited) {
        if (cnt == k) {
            result++;
            return;
        }

        for (int i = index; i < subjects.size(); i++) {
            Subject subject = subjects.get(i);
            if (isPossible(subject, visited)) {
                changeVisitedStatus(subject, visited, true);
                backTracking(k, cnt + subject.point, i + 1, subjects, visited);
                changeVisitedStatus(subject, visited, false);
            }
        }
    }

    private static void changeVisitedStatus(Subject subject, boolean[][] visited, boolean status) {
        for (int i = subject.start; i <= subject.end; i++) {
            visited[subject.dayOfWeek][i] = status;
        }
    }

    private static boolean isPossible(Subject subject, boolean[][] visited) {
        for (int i = subject.start; i <= subject.end; i++) {
            int dayOfWeek = subject.dayOfWeek;
            if (visited[dayOfWeek][i]) {
                return false;
            }
        }
        return true;
    }
}
