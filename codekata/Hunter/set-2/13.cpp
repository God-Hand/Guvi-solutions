#include<bits/stdc++.h>
using namespace std;

int main(){
    string str;
    getline(cin, str);
    stack<char> s;
    int _size = str.size()/2;
    for(int i=0; i<_size; i++)
        s.push(str[i]);
    for(int i=str.size() - _size; i<str.size(); i++){
        char c=s.top();
        s.pop();
        if(c!=str[i])
            break;
    }
    if(s.empty())
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}
