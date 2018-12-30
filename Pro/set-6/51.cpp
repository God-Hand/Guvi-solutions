#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    vector<int> arr(n);
    arr[n-1]=1;
    for(int i=n-2; i>=0; i--){
        if((vec[i]>0 && vec[i+1]<0) || (vec[i]<0 && vec[i+1]>0))
            arr[i] = arr[i+1]+1;
        else
            arr[i] = 1;
    }
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
	return 0;
}
