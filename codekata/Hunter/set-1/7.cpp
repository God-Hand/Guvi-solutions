#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<iterator>
#include<map>
using namespace std;

int main(){
    int n, temp;
    cin>>n;
    map<int,int> m;
    for(int i=0; i<n; i++){
        cin>>temp;
        if( (temp+i)%2 )
            cout<<temp<<" ";
    }
    return 0;
}
