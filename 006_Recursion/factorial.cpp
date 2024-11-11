// we are finding the factorial of the given number:
#include<bits/stdc++.h>
using namespace std;// time complexity : O(n), space complexity : O(n).

#define ll long long                //! page no : 27.

int factorial(int n){           // if the number is 0 , then it will return 1.
    if(n == 0) return 1;
    return n*factorial(n-1);            // otherwise it will return n*factorial(n-1)
}
int main() {
    int n = 0;
    cout << factorial(n) << endl;
    return 0;
}