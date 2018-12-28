#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int log_n = log2(n);
    if(pow(2, log_n) == n)
        cout<<0;
    else
        cout<<pow(2, log_n+1) - n;
    return 0;
}
