class Solution {
    static boolean solution(String s) {
        int p = (int) s.toLowerCase()
            .chars()
            .filter(ch -> ch == 'p')
            .count();
        
        int c = (int) s.toLowerCase()
            .chars()
            .filter(ch -> ch == 'y')
            .count();
        
        return (p == c) ? true : false;
    }
}