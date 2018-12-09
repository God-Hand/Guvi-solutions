#include<iostream>
#include<vector>
#include<map>
using namespace std;

void printUnique(int n, vector<int> vec){
    bool unique_flag = true;
    sort(vec.begin(),vec.end());
    for(int i=1; i<n; i++){
        if(vec[i]==vec[i-1]){
            cout<<vec[i]<<" ";
            unique_flag = false;
        }
    }
    if(unique_flag){
        cout<<"unique";
    }
}

int main(){
    int n,temp;
    vector<int> vec;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>temp;
        vec.push_back(temp);
    }
    printUnique(n,vec);
    return 0;
}
