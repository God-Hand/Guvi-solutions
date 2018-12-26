#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

string LCS(string A, string B){
    int n=A.size(), m=B.size();
    int continuous[n+1][m+1] = {0}, lmax = 0, pos;
    string return_str = "";
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(A[i-1]==B[j-1]){
                continuous[i][j] = continuous[i-1][j-1] + 1;
            }else{
                continuous[i][j] = max(continuous[i-1][j], continuous[i][j-1]);
            }
            if(lmax<continuous[i][j]){
                lmax = continuous[i][j];
                pos = i;
            }
        }
    }
    int i=n, j=m, previous=continuous[i][j]+1;
    while(continuous[i][j]!=0){
        if(previous>continuous[i][j]){
            return_str += B[j-1];
        }
        previous = continuous[i][j];
        if(continuous[i-1][j] < continuous[i][j-1])
            i-=1;
        else
            j-=1;
    }
    reverse(return_str.begin(), return_str.end());
    return return_str;
}

int main(){
    string A, B;
    cin>>A>>B;
    cout<<LCS(A,B)<<endl;
    return 0;
}
