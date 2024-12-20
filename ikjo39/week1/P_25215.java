import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class P_25215 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        char[] inputs = br.readLine().toCharArray();

        int result = getResult(inputs);
        bw.write(result + System.lineSeparator());
        bw.flush();
    }

    private static int getResult(char[] inputs) {
        boolean isRhombus = false;
        int count = inputs.length;

        for (int i = 0; i < inputs.length - 1; i++) {
            char now = inputs[i];
            char next = inputs[i + 1];
            if (isCorrectOrder(isRhombus, now)) {
                continue;
            }
            if (hasToPress(isRhombus, now, next)) {
                count++;
                isRhombus = !isRhombus;
            } else {
                count++;
            }
        }

        int lastIndex = inputs.length - 1;
        if (!isCorrectOrder(isRhombus, inputs[lastIndex])) {
            count++;
        }

        return count;
    }

    private static boolean hasToPress(boolean isRhombus, char now, char next) {
        return (!isRhombus && Character.isUpperCase(now) && Character.isUpperCase(next))
                || (isRhombus && Character.isLowerCase(now) && Character.isLowerCase(next));
    }

    private static boolean isCorrectOrder(boolean isRhombus, char c) {
        return (!isRhombus && Character.isLowerCase(c))
                || (isRhombus && Character.isUpperCase(c));
    }
}
