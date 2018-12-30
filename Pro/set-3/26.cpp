#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, max_count=0;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    for(int i=0; i<n-1; i++){
        int count = 1, previous = arr[i];
        for(int j=i+1; j<n; j++){
            if(arr[j] > previous){
                previous = arr[j];
                count++;
            }
        }
        max_count = max(max_count, count);
    }
    cout<<max_count<<endl;
    return 0;
}
