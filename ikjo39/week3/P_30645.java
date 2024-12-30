import java.util.Arrays;
import java.util.Scanner;

public class P_30645 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int R = sc.nextInt();
        int C = sc.nextInt();
        int N = sc.nextInt();

        int[] h = new int[N];
        int[] map = new int[C];

        for (int i = 0; i < N; i++) {
            h[i] = sc.nextInt();
        }

        Arrays.sort(h);

        int index = 0, cnt = 0;

        for (int i = 0; i < N; i++) {
            if (h[i] > map[index]) {
                map[index] = h[i];
                ++cnt;
                index = (index + 1) % C;
            }
        }

        if (cnt > R * C) {
            cnt = R * C;
        }

        System.out.println(cnt);
    }
}
