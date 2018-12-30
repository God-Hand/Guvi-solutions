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
    bool is_present[26] = {false};
    for(int i=0; i<input.length(); i++){
        if(is_present[input[i]-'a'])
            continue;
        cout<<input[i];
        is_present[input[i]-'a'] = true;
    }
    return 0;
}
