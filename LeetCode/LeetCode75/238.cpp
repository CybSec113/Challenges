#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int max = nums.size();
        vector<int> result(max, 0);
        vector<int> pre(max,0);
        vector<int> suff(max,0);

        // build prefix vector
        pre[0] = 1;
        for (int i=1; i<max; i++)
            pre[i] = pre[i-1] * nums[i-1];

        // build suffix vector
        suff[max-1] = 1;
        for (int i=max-2; i>=0; i--)
            suff[i] = suff[i+1] * nums[i+1];

        // build result vector
        for (int i=0; i < max; i++)
            result[i] = pre[i] * suff[i];

        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2,3,4,5,6,7};
    vector<int> res = sol.productExceptSelf(nums);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}