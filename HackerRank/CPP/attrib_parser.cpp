// need to revisit this approach and implementation


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

class Parser {
private:
    vector<string> source;
    vector<string> queries;

public:
    Parser(vector<string> source) {
        Parser::source = source;
    }

    string parseSource(vector<string> tagv, string value) {
        string result = "empty";
        int nest=0;

        string tag;
        if (tagv.size() == 1) {
            tag = tagv[0];
            for (string s : source) {
                if (s.find(tag)) {
                    cout << "source: " << s << endl;
                    int start = s.find(tag)+tag.length()+5;
                    int end = s.find('"', start+1);
                    cout << "start,end: " << start << ", " << end << endl;
                    result = s.substr(start, end);
                }
            }
        } else {

        }

        return result;
    }

    string parseTags(string query) {
        string value;
        vector<string> tagv;

        // get query value
        value = query.substr(query.find('~')+1, query.length()); 

        // get individual query tags
        query = query.substr(0, query.find('~'));
        string tag;
        int pos=0;
        while ((pos=query.find('.')) != std::string::npos) {
            tag = query.substr(0, pos);
            tagv.push_back(tag);
            query.erase(0, pos+1);
        }
        tagv.push_back(query);

        return parseSource(tagv, value);
    }
};

int main() {
    vector<string> source;
    vector<string> queries;
    vector<string> values;
    string line;
    int N,Q=0;

    cin >> N >> Q;
    for (int i=0; i<=N; i++) {
        std::getline(cin, line);
        source.push_back(line);
    }

    for (int i=0; i<Q; i++) {
        std::getline(cin, line);
        queries.push_back(line);
    }

    Parser parser(source);
    for (string s : queries)
        cout << parser.parseTags(s) << endl;

    return 0;
}
