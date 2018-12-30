#include<stdio.h>
#include<iostream>
using namespace std;

int knapSack(int W, int n, int w[], int val[]) {
    int k[n+1][W+1] = {0};
    for(int i=0; i<=n; i++){
        for(int j=0; j<=W; j++){
            if( i == 0 || j == 0 )
                k[i][j] = 0;
            else if( w[i-1] <= j )
                k[i][j] = max( k[i-1][j-w[i-1]] + val[i-1], k[i-1][j] );
            else
                k[i][j] = k[i-1][j];
        }
    }
    return k[n][W];
}

int main(){
    int n, w;
    cin>>n>>w;

    int wt[n];
    int val[n];
    for(int i=0; i<n; i++)
        cin>>wt[i];
    for(int i=0; i<n; i++)
        cin>>val[i];
	cout<<knapSack(w, n, wt, val);
	return 0;
}
