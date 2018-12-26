#include<iostream>
#include<algorithm>
#include<map>
#include<iterator>
using namespace std;

map<int,int> m;

int main(){
    int n, temp, sum=0;
    cin>>n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin>>temp;
            if(i==j){
                sum+=temp;
            }
        }
    }
    cout<<sum;
    return 0;
}
