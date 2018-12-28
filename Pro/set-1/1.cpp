#include<bits/stdc++.h>
using namespace std;

int main(){
    int i, n, min_length=INT_MAX;
    cin>>n;
    vector<string> vec(n);
    string min_string;
    for(int i=0; i<n; i++){
        cin>>vec[i];
        if(min_length > vec[i].length()){
            min_length = vec[i].length();
            min_string = vec[i];
        }
    }

    bool stop = false;
    for(i=0; i<min_length; i++){
        for(int j=0; j<n; j++){
            if(vec[j][i] != min_string[i]){
                stop = true;
                break;
            }
        }
        if(stop)
            break;
    }
    if(!stop)
        cout<<min_string;
    else
        cout<<min_string.substr(0,i-1);
    return 0;
}
