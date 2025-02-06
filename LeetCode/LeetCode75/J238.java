public class J238 {
    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        Solution sol = new Solution();
        int[] ans = sol.productExceptSelf(nums);
        for (int n : ans) {
            System.out.print(n + ", ");
        }
    }
}

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        return result;
    }
}