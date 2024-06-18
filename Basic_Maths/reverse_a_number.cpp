// basically we will reverse the number that is given.

#include<bits/stdc++.h>         //! page no : 2
using namespace std;

#define ll long long
int optimal_approach(int n){
    int rev_no = 0;
    while(n > 0){
        int ld  = n%10;                 //taking the last digit.
        rev_no = rev_no * 10 + ld;          // storing the last digit in the reverse number.
        n /= 10;                          // removing the last digit.
    }
    return rev_no;
}

int main() {
    int n = 1234;
    cout << optimal_approach(n) << endl;
    return 0;
}