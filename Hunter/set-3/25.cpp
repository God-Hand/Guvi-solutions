#include<bits/stdc++.h>
using namespace std;

int findLCA(int n1, int n2, vector<int> vec) {
    vector<bool> visited(vec.size(), false);

    visited[n1] = true;
    while (n1 != 0) {
        visited[n1] = true;
        n1 = n1/2;
    }

    visited[n1] = true;
    while (!visited[n2])
        n2 = n2/2;
    return vec[n2];
}

int main(){
    int n, u, v;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    cin>>u>>v;
    cout<<findLCA(u, v, vec);
    return 0;
}
