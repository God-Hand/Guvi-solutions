#include<bits/stdc++.h>
using namespace std;

int getMaxValue(int row, int col, vector<vector<int>> &vec){
    vector<vector<int>> val(row+1, vector<int>(col+1));
    for(int i=0; i<=row; i++){
        for(int j=0; j<=col; j++){
            if(i==0 || j==0){
                val[i][j] = 0;
                continue;
            }
            val[i][j] = max(val[i][j-1], val[i-1][j]) + vec[i-1][j-1];
        }
    }
    return val[row][col];
}

int main(){
    int row, col;
    cin>>row>>col;

    vector<vector<int>> vec(row, vector<int>(col));
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            cin>>vec[i][j];
        }
    }
    cout<<getMaxValue(row, col, vec);
    return 0;
}
