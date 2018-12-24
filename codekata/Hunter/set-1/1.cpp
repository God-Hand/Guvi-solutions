#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<iterator>
#include<set>
using namespace std;

int main(){
    int n, temp;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    sort(vec.begin(), vec.end());
    set<int> s;
    for(int i=1; i<n; i++){
        if(vec[i]==vec[i-1])
            s.insert(vec[i]);
    }
    if(s.size() == 0)
        cout<<"unique";
    for(auto i : s){
        cout<<i<<" ";
    }
}
