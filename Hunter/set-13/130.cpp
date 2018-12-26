#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

bool isPrime(int n){
    for(int i=2; i<=((int)sqrt(n)); i++){
        if(!(n%i))
            return false;
    }
    return true;
}
int main(){
    int n, sum=0;
    cin>>n;
    for(int i=3; i<=n; i+=10){
        if(isPrime(i))
            sum+=i;
    }
    cout<<sum;
    return 0;
}
