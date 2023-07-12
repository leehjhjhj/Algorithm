import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;


class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String, Integer> score = new HashMap<>();
        int[] answer = new int[photo.length];

        for (int i = 0; i < name.length; i++) {
            score.put(name[i], yearning[i]);
        }

        for (int i = 0; i < photo.length; i++) {
            int rst = 0;
            for (int j = 0; j < photo[i].length; j++) {
                rst += score.getOrDefault(photo[i][j], 0);
            }
            answer[i] = rst;
        }
        return answer;
    }
}
