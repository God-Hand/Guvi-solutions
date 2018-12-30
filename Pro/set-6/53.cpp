#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    bool visited[26];
    memset(visited, false, sizeof(visited));
    getline(cin, s);
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    int total = 0;
    for(int i=0; i<s.length(); i++){
        if(s[i]>='a' && s[i]<='z' && !visited[s[i]-'a']){
            total++;
            visited[s[i]-'a'] = true;
        }
    }
    if(total==26)
        cout<<"yes";
    else
        cout<<"no";
    return 0;
}
