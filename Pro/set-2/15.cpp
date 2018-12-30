#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    vector<int> vec(n);
    for(int i=0; i<n; i++)
        cin>>vec[i];

    sort(vec.begin(), vec.end(), [](int a, int b){
        bitset<16> b1(a), b2(b);
        if(b1.count()!=b2.count())
            return b1.count()>b2.count();
        else
            return a>b;
    });
    for(int i=0; i<n; i++){
        cout<<vec[i]<<endl;
    }
    return 0;
}
