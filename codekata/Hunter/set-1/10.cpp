#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m;
    cin>>n>>m;
    vector<int> a(n);
    vector<int> b(m);
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    sort(a.begin(), a.end());
    for(int i=0; i<m; i++){
        cin>>b[i];
    }
    sort(b.begin(), b.end());
    int j=0, i=0;
    while(j<m && i<n){
        if(b[j]==a[i]){
            j++;
        }
        i++;
    }
    if(j==m)
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}
