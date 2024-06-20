// we are printing 1 to n using recursion.
#include<bits/stdc++.h>
using namespace std;                        //! page no : 24.

#define ll long long

void func(int n){
    if(n > 1) func(n-1);                          // time complexity : O(n) and space complexity : O(n). placing of these two lines is important, if i put this line up first, then it will print from 1 to n.
    cout << n << endl;          // other wise it would print n to 1.
}

int main() {
    int n; n = 17;
    func(n);
    return 0;
}