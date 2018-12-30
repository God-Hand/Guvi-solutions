#include<bits/stdc++.h>
using namespace std;

int main(){
    string input;
    cin>>input;
    int num = 0;

    if(input.length()>3)
        num = stoi(input.substr(input.length()-3, input.length()));
    else
        num = stoi(input);
    if(num%8==0)
        cout<<"YES";
    else
        cout<<"NO";
	return 0;
}
