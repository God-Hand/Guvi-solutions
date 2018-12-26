#include<iostream>
#include<algorithm>
#include<map>
#include<iterator>
using namespace std;

map<int,int> m;

int main(){
    int n;
    cin>>n;
    int min=1000000, temp;
    map<int, int>::iterator it;
    for(int i=0; i<n; i++){
        cin>>temp;
        it = m.find(temp);
        if(it == m.end()){
            m.insert(make_pair(temp, 1));
        }else{
            m[temp] += 1;
        }
        if(m[min]<m[temp]){
            min = temp;
        }else if(min>temp && m[min]<m[temp]){
            min = temp;
        }
    }
    cout<<min;
}
