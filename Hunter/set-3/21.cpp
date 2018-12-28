#include<bits/stdc++.h>
using namespace std;

void changeRowCol(int row, int col, vector<vector<int>> &vec){
    for(int i=0; i<vec.size(); i++)
        vec[i][col] = 0;
    for(int i=0; i<vec[row].size(); i++)
        vec[row][i] = 0;
}

int main(){
    int row, col;
    cin>>row>>col;

    vector<vector<int>> vec(row, vector<int>(col));
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            cin>>vec[i][j];
            if(vec[i][j]==0)
                vec[i][j] = INT_MAX;
        }
    }

    for(int i=0; i<row; i++)
        for(int j=0; j<col; j++)
            if(vec[i][j] == INT_MAX)
                changeRowCol(i, j, vec);

    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            cout<<vec[i][j]<<" ";
        }
        cout<<endl;
    }
}
