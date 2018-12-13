#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int sum = 0;

int digitPow(int n){
    int digit_pow = 1;
    if(n<10){
        sum += 1;
        return 0;
    }
    digit_pow += digitPow(n/10);
    sum += pow(n%10, digit_pow);
    return digit_pow;
}

int main(){
    int n;
    cin>>n;
    int temp = digitPow(n);
    cout<<sum;
    return 0;
}
