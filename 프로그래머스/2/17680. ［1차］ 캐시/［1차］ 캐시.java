import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Deque<String> cache = new LinkedList<>();
        
        for (String city : cities) {
            String tmp = city.toUpperCase();
            
            if (cache.contains(tmp)) {
                cache.remove(tmp);
                cache.add(tmp);
                answer += 1;
            } else {
                if (cache.size() == cacheSize) {
                    cache.add(tmp);
                    cache.removeFirst();
                    answer += 5;
                } else {
                    cache.add(tmp);
                    answer += 5;
                }
            }
            
        }

        return answer;
    }
}