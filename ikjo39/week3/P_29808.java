import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;

public class P_29808 {

    static final int ZIP_CODE = 4763;
    static final int KOR_BIGGER_ENG = 508;
    static final int KOR_NOT_BIGGER_ENG = 108;
    static final int MATH_BIGGER_TAM = 212;
    static final int MATH_NOT_BIGGER_TAM = 305;
    static final int[] KOR_ENG = {KOR_BIGGER_ENG, KOR_NOT_BIGGER_ENG};
    static final int[] MATH_TAM = {MATH_BIGGER_TAM, MATH_NOT_BIGGER_TAM};
    static Set<List<Integer>> standardScores;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int hakbun = Integer.parseInt(br.readLine());
        standardScores = new HashSet<>();
        calculateNumberOfCases(hakbun);
        bw.write(standardScores.size() + System.lineSeparator());

        List<String> results = standardScores.stream()
                .sorted((o1, o2) -> {
                    if (Objects.equals(o1.get(0), o2.get(0))) {
                        return o1.get(1) - o2.get(1);
                    }
                    return o1.get(0) - o2.get(0);
                })
                .map(score -> score.get(0) + " " + score.get(1))
                .collect(Collectors.toList());

        for (String result : results) {
            bw.write(result + System.lineSeparator());
        }
        bw.flush();
    }

    private static void calculateNumberOfCases(int hakbun) {
        if (hakbun % ZIP_CODE != 0) {
            return;
        }

        if (hakbun == 0) {
            standardScores.add(List.of(0, 0));
        }

        hakbun /= ZIP_CODE;

        for (int i = 0; i < 201; i++) {
            for (int j = 0; j < 201; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }
                addIfSatisfiedCondition(i, j, hakbun);
            }
        }
    }

    private static void addIfSatisfiedCondition(int korEng, int mathTam, int condition) {
        for (int korEngPoint : KOR_ENG) {
            for (int mathTamPoint : MATH_TAM) {
                int result = korEngPoint * korEng + mathTamPoint * mathTam;
                if (condition == result) {
                    standardScores.add(List.of(korEng, mathTam));
                }
            }
        }
    }
}
