import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        Map<String, int> score = new HashMap<>();
        List<int> answer = new List<>();
        
        for (int i; i < name.length; i++) {
            score.put(name[i], yearning[i]);
        }
        for (int i; i < photo.length; i++) {
            int rst = 0;
            for (int j; j < photo[i].length; j++) {
                rst += score.get(photo[i][j]);
            }
            answer.add(rst);
            rst = 0;
        }
        //List<int> result = Arrays.asList(answer);
        return answer;
    }
}
