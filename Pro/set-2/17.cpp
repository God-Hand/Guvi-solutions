#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, k;
    cin>>n>>k;

    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    sort(vec.begin(), vec.end());
    bool flag = true;
    for(int i=0; i<n-1; i++){
        if(find(vec.begin()+i, vec.end(), k-vec[i]) != vec.end()){
            flag = false;
            cout<<"yes";
            break;
        }
    }
    if(flag)
        cout<<"no";
    return 0;
}
