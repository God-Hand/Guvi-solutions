#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

string str;
int longestPalindrome(int center, int n, int i){
    if(center-i==-1 || center+i==n || str[center-i]!=str[center+i]){
        return 0;
    }
    if(str[center-i]=='|'){
        return longestPalindrome(center, n, i+1);
    }
    return 1+longestPalindrome(center, n, i+1);
}

int main(){
    string input;
    cin>>input;
    int n,max_length=0,pos,length;
    n = input.length();
    str="";
    for(int i=0; i<n-1; i++){
        str.push_back(input[i]);
        str.push_back('|');
    }
    str.push_back(input[n-1]);
    for(int i=0; i<str.length(); i++){
        length = 1+longestPalindrome(i,str.length(),1);
        if(max_length<length){
            max_length=length;
            pos = i;
        }
    }
    for(int i=pos-2*(max_length-1); i<pos+2*(max_length)-1; i++){
        if(str[i]!='|')
            cout<<str[i];
    }
    return 0;
}
