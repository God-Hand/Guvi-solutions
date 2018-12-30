#include<bits/stdc++.h>
using namespace std;

int distanceSquare(int x1, int y1, int x2, int y2){
    return ((x1-x2)*(x1-x2)) + ((y1-y2)*(y1-y2));
}

int main(){
    int x1,x2,x3,x4;
    int y1,y2,y3,y4;
    cin>>x1>>y1;
    cin>>x2>>y2;
    cin>>x3>>y3;
    cin>>x4>>y4;

    int l1 = distanceSquare(x1, y1, x2, y2);
    int l2 = distanceSquare(x1, y1, x4, y4);
    int l3 = distanceSquare(x3, y3, x4, y4);
    int l4 = distanceSquare(x3, y3, x2, y2);
    int d1 = distanceSquare(x1, y1, x3, y3);
    int d2 = distanceSquare(x2, y2, x4, y4);

    if(l1==l2 && l2==l3 && l3==l4 && d1==2*l1 && d2==2*l1)
        cout<<"yes";
    else
        cout<<"no";
}
