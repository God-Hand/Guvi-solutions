#include<bits/stdc++.h>
using namespace std;

bool isPrime(int n){
    for(int i=2; i<sqrt(n); i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    int n;
    cin>>n;
    int arr[3];

    if(n&1){ arr[0] = 2; n -= 2;
    }else{ arr[0] = 3; n -= 3; }

    for(int i=2; i<n-1; i++){
        if(isPrime(i) && isPrime(n-i)){
            arr[1] = i;
            arr[2] = n-i;
            break;
        }
    }
    sort(arr, arr+3);
    cout<<arr[0]<<" "<<arr[1]<<" "<<arr[2];
    return 0;
}
