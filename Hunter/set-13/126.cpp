#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int main(){
    string str;
    bool flag=false;
    getline(cin,str);
    for(int i=0; i<str.length(); i++){
        if(isupper(str[i]) && (i==0 || str[i-1]==' ')){
            flag=true;
        }
    }
    if(flag){
        cout<<"yes";
    }else{
        cout<<"no";
    }
    return 0;
}
