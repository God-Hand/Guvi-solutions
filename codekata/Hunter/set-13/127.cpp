#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

string LCSSubStr(string A, string B){
    int n=A.size(), m=B.size();
    int continuous[n+1][m+1] = {0}, max = 0, pos;
    string return_str = "";
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(A[i-1]==B[j-1]){
                continuous[i][j] = continuous[i-1][j-1] + 1;
            }
            if(max<continuous[i][j]){
                max = continuous[i][j];
                pos = i;
            }
        }
    }
    for(int i=pos-max; i<pos; i++){
        return_str += (A[i]);
    }
    return return_str;
}

int main(){
    string A, B;
    cin>>A>>B;
    cout<<LCSSubStr(A,B)<<endl;
    return 0;
}
