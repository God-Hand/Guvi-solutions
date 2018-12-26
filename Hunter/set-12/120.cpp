#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<iterator>
using namespace std;

int main(){
    int n;
    long int count=0;
    cin>>n;
    vector<int> arr(n);
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    for(int k=2; k<n; k++){
        for(int j=1; j<k; j++){
            for(int i=0; i<j; i++){
                if(arr[k] == arr[j]+arr[i] ){
                    count++;
                }
            }
        }
    }
    cout<<count<<endl;
    return 0;
}
