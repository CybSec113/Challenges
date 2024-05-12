#include <iostream>
#include <exception>
#include <string>
#include <stdexcept>
#include <vector>
#include <cmath>
using namespace std;

class Server {
private:
	static int load;
public:
	static int compute(long long A, long long B) {
		load += 1;
		if(A < 0) {
			throw std::invalid_argument("A is negative");
		}
		vector<int> v(A, 0);
		int real = -1, cmplx = sqrt(-1);
		if(B == 0) throw 0;
		real = (A/B)*real;
		int ans = v.at(B);
		return real + A - B*ans;
	}
	static int getLoad() {
		return load;
	}
};
int Server::load = 0;

int main() {

    long A=3850;
    long B=921492;
		/* Enter your code here. */
    try {
        cout << Server::compute(A,B) << endl;
    }
    catch (std::invalid_argument arg) { cout << "Exception: " << arg.what() << endl; }
    catch (std::bad_alloc arg) { cout << "Not enough memory" << endl; }
    catch (std::exception &e) { cout << "Exception: " << e.what() << endl; }
    catch (...) { cout << "Other Exception" << endl; }


	cout << Server::getLoad() << endl;
	return 0;
}