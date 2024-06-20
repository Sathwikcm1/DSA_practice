// check if the string is palindrome or not.
#include<bits/stdc++.h>
using namespace std;                        //! page no : 27.

#define ll long long

bool check(string s, int i, int n){ 
    if ( i >= n/2) return true;         // again we check till the half of the string. 
    if(s[i] != s[n-i-1]) return false;  // if the ith character and the n-ith character is not equal, we return false.
    return check(s,i+1,n);              // other wise we call the function again but with i+1.
}
int main() {
    string s = "madam";
    int n = s.length();
    cout <<check(s,0,s.length()) << endl;

    return 0;
}   