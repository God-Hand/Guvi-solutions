#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<array>
using namespace std;

bool isPrime(int n){
    for(int i=2; i<=(int)sqrt(n); i++){
        if(!(n%i))
            return false;
    }
    return true;
}

vector<bool> primeNumbers(int n){
    vector<bool> primes(n+1, false);
    for(int i=2; i<=n; i++){
        primes[i]=isPrime(i);
    }
    return primes;
}

int main(){
    int n, i=2, max=1001, count=0;
    cin>>n;
    vector<bool> primes = primeNumbers(n-2);
    while( i<max ){
        if(primes[i] && primes[n-i]){
            count += 1;
            max = n-i;
            cout<<i<<" "<<n-i<<endl;
        }
        i++;
    }
    cout<<count;
    return 0;
}
