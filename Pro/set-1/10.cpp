#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    long int sum = 0;
    cin>>n;
    vector<int> vec(n);
    vector<long int> sum_v(n+1);
    sum_v[0] = 0;
    for(int i=0; i<n; i++){
        cin>>vec[i];
        sum_v[i+1] = 0;
        for(int j=0; j<i; j++){
            if(vec[i]>vec[j])
                sum_v[i+1] += vec[j];
        }
        sum += sum_v[i+1];
    }
    cout<<sum<<endl;
    return 0;
}
