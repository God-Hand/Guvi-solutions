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

vector<bool> primeNumbers(){
    vector<bool> primes(46, false);
    for(int i=2; i<=45; i++){
        primes[i]=isPrime(i);
    }
    return primes;
}

int digitSum(int n){
    if(n<10)
        return n;
    return n%10 + digitSum(n/10);
}

int main(){
    vector<bool> primes = primeNumbers();
    int a, b, count=0;
    cin>>a>>b;
    for(int i=a; i<=b; i++){
        count += primes[digitSum(i)];
    }
    cout<<count;
    return 0;
}
