#include <iostream>

using namespace std;

class Solution {
public:
    int kthFactor(int n, int k) {
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                k--;
                if (k == 0) {
                    return i;
                }
            }
        }
        return -1;
    }
};

int main()
{
    Solution sol;
    int n = 4, k = 4;
    cout << sol.kthFactor(n, k) << endl;
    return 0;
}