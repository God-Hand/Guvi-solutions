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
    for(int i=0; i<n; i++){
        cin>>temp;
        if(temp==i)
            cout<<temp<<" ";
    }
    return 0;
}
