#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
	long long P = 3;
	while(n>P){
		n -= P;
		P *= 2;
	}
	cout << P - n + 1 << endl;
    return 0;
}
