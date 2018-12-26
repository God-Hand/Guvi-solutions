#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, temp;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    sort(vec.begin(), vec.end());
    int mindiff = INT_MAX;
    int a,b;
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            temp = vec[j] + vec[i];
            if(temp<mindiff && temp>=0){
                mindiff = temp;
                a=vec[j];
                b=vec[i];
            }
        }
    }
    cout<<a<<" "<<b;
    return 0;
}
