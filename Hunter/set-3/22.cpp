#include<bits/stdc++.h>
using namespace std;

long int getProduct(vector<long int> vec){
    long int product = 1;
    for(int i=0; i<vec.size(); i++){
        product *= vec[i];
    }
    return product;
}

int main(){
    int n;
    cin>>n;

    vector<long int> vec(n);
    for(int i=0; i<n; i++){
        cin>>vec[i];
        if(vec[i]==0)
            vec[i]=1;
    }

    long int product = getProduct(vec);

    for(int i=0; i<n; i++)
        cout<<(long int)product/vec[i]<<" ";

    return 0;
}
