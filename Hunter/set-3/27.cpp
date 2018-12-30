#include<bits/stdc++.h>
using namespace std;

bool isPalindrome(string s) {
    if(s.length() <= 1)
        return true;
    if(s[0] == s[s.length()-1] && s.length()>0)
        return isPalindrome(s.substr(1,s.length()-2));
    return false;
}

int main(){
    string input;
    cin>>input;
    while(true){
        if(isPalindrome(input)){
            input = input.substr(0, input.length()-1);
        }else{
            break;
        }
    }
    cout<<input;
    return 0;
}
