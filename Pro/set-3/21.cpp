#include<bits/stdc++.h>
using namespace std;

string equalAveragePartition(vector<int> arr){
	int sum = 0;
	int n = arr.size();
	for(int i = 0; i < n; i++)
		sum += arr[i];

	int lsum = 0;
	for(int i = 0; i < n-1; i++){
		lsum += arr[i];
		int rsum = sum - lsum;
     	if (lsum * (n - i - 1) == rsum * (i + 1)) {
			return "yes";
		}
	}
  	return "no";
}

int main() {
    int n;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    cout<<equalAveragePartition(vec)<<endl;
	return 0;
}
