public class J151 {
    public static void main(String[] args) {
        String s = "the sky is blue";
        Solution sol = new Solution();
        System.out.println(sol.reverseWords(s));

        s = "   the sky     is blue   ";
        System.out.println(sol.reverseWords(s));
    }
}

class Solution {
    public String reverseWords(String s) {
        String result = "";
        String[] words = s.trim().split(" ");
        for (String w : words) {
            if (w == "")
                continue;
            result = w + "*" + result;
        }
        result = result.substring(0, result.length() - 1);
        return result;
    }
}