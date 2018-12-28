/* it ask for possible case where
s1={a,b} and s2={b,a}
thus, for a!=b  x must be atleast 2 time multiple
*/
#include<bits/stdc++.h>

using namespace std;

int main(){
    long long int x,a,b;
    cin>>x>>a>>b;
    if((x/2)%(a+b)==0 && x%2==0)
        cout<<"YES";
    else if(a==b && (x/2)%a==0 && x%2==0)
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}
