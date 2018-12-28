#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, count_triplet = 0;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }

    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++){
            if(vec[i] < vec[j]){
                for(int k=j+1; k<n; k++){
                    if(vec[j] < vec[k]){
                        count_triplet++;
                    }
                }
            }
        }
    }
    cout<<count_triplet;
    return 0;
}
