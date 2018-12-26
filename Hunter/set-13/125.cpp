#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int main(){
    string str;
    cin>>str;
    int arr[50]={0};
    for(int i=0; i<str.length(); i++){
        arr[str[i]-65]+=1;
    }
    for(int i=0; i<str.length(); i++){
        if(arr[str[i]-65]==1)
            cout<<str[i];
    }
    return 0;
}
