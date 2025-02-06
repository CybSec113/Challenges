#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string result = "";
        string word = "";
        for (char c : s) {
            if (c == ' ' && word == "") {
                continue;
            }
            if (c == ' ') {
                result = word + "*" + result;
                word = "";
            } else {
                word = word + c;
            }
        }
        if (word != "")
            result = word + "*" + result;
        result = result.erase(result.size() - 1);
        return result;
    }
};

int main() {
    Solution s;
    string str = "the sky is blue";
    cout << s.reverseWords(str) << endl;

    str = "       the sky        is blue       ";
    cout << s.reverseWords(str) << endl;
    return 0;
}