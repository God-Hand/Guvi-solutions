// Manacher's algorithm
#include<bits/stdc++.h>

using namespace std;

int longestPalindrome(int center, int i, string str){
    if(center-i==-1 || center+i==str.length() || str[center-i]!=str[center+i]){
        return 0;
    }
    if(str[center-i]=='|'){
        return longestPalindrome(center, i+1, str);
    }
    return 1+longestPalindrome(center, i+1, str);
}

void printPalindromes(string str){
    int length;
    string new_string  = "";
    string output = "";

    set<string> s;
    s.insert("");
    for(int i=0; i<str.length()-1; i++){
        new_string.push_back(str[i]);
        new_string.push_back('|');
    }
    new_string.push_back(str[str.length()-1]);
    for(int i=0; i<new_string.length(); i++){
        length = longestPalindrome(i, 1, new_string);
        if(1<length){
            int start = i - length*2, finish = i + length*2 + 1;
            while(start < finish){
                output = "";
                for(int k=start; k<finish; k++){
                    if(new_string[k] != '|')
                        output.push_back(new_string[k]);
                }
                start += 2;
                finish -= 2;
                if(output.length()>1)
                    s.insert(output);
            }
        }
    }
    s.erase(s.find(""));
    vector<string> out;
    for(auto it = s.begin(); it!=s.end(); it++){
        out.push_back(*it);
    }
    sort(out.begin(), out.end(), [](string s1, string s2){
        if(s1.length()==s2.length())
            return s1 < s2;
        return s1.length()<s2.length();
    });
    for(int i=0; i<out.size(); i++){
        cout<<out[i]<<endl;
    }
}

int main(){
    string input;
    cin>>input;
    printPalindromes(input);
    return 0;
}
