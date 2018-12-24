#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int n, temp;
    cin>>n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }
    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++){
            for(int k=j+1; k<n; k++){
                if(vec[i]+vec[j]==vec[k])
                    cout<<vec[i]<<" "<<vec[j]<<" "<<vec[k]<<endl;
            }
        }
    }
    return 0;
}
