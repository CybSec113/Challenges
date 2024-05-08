#include <iostream>
#include <deque> 
#include <algorithm>
using namespace std;

void printKMax(int arr[], int n, int k){
	//Write your code here.
    deque<int> subarr;

    for (int i=0; i<k; i++)
        subarr.push_front(arr[i]);
    auto max = *max_element(subarr.begin(), subarr.end());

    for (int i=k; i<n; i++) {
        cout << max << " ";
        int last = subarr.back();
        subarr.pop_back();
        subarr.push_front(arr[i]);
        if (subarr.front() > max)  // if new element is > max, it's the new max!
            max = subarr.front();
        if (last == max)  // max is leaving deque, need to recompute max from scratch!
            max = *max_element(subarr.begin(), subarr.end());
    }
    cout << max << endl;
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}