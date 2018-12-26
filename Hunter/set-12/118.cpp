#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    string input;
    cin>>input;
    int sum = 0;
    for( int i=0; i<input.size(); i++){
        sum += (int)input[i];
    }
    cout<<sum;
    return 0;
}
