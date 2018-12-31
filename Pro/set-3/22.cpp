#include<bits/stdc++.h>
using namespace std;

int maxSumWithoutNeighbours(vector<int> vec){
    int include = vec[0];
    int exclude = 0;
    int temp_exclude = 0;
    for(int i=1; i<vec.size(); i++){
        temp_exclude = max(include , exclude);
        include = exclude + vec[i];
        exclude = temp_exclude;
    }
    return max(include, exclude);
}

int main(){
    int n;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++)
        cin>>vec[i];
    cout<<maxSumWithoutNeighbours(vec);
    return 0;
}
