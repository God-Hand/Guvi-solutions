#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

string prepend(string s, int m){
    string str = "";
    str += s;
    for(int i=1; i<=m-s.size(); i++){
        str += to_string(i);
    }
    cout<<str<<endl;
    return str;
}

int main(){
    string A, B, password="";
    cin>>A>>B;
    if( A.size()<B.size() )
        A = prepend(A,B.size());
    else if( A.size()>B.size() )
        B = prepend(B, A.size());
    for(int i=0; i<=A.size(); i++){
        password += A[i];
        password += B[i];
    }
    cout<<password<<endl;
    return 0;
}
