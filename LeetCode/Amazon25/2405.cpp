#include <iostream>
#include <map>
#include <string>

using namespace std;

class Solution {
public:
    int partitionString(string s) {
        int mp[26] = {0};
        int res = 0;
        for (char c : s) {
            if (mp[c-97] > 0) {
                res++;
                for (int i=0; i<26; i++) {mp[i] = 0;};
            }
            mp[c-97]++;
        }
        return res+1;
    }
};

int main()
{
    Solution sol;
    string s = "abacaba";
    cout << sol.partitionString(s) << endl;
    return 0;
}