#include<bits/stdc++.h>
using namespace std;

int main(){
    string str;
    getline(cin, str);
    istringstream s(str);
    vector<string> st;
    do{
        s>>str;
        st.push_back(str);
    }while(s);
    for(int i=0; i<st.size()-1; i++){
        reverse(st[i].begin(), st[i].end());
        cout << st[i] << " ";
    }
    return 0;
}
