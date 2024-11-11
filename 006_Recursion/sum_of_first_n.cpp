// we are basically printing the sum of the first n natural numbers.

#include<bits/stdc++.h>
using namespace std;

#define ll long long
void func(int n, int sum){          // we take sum as an argument to store the sum of the first n natural numbers.  , if n is zero , that means it's the end  we print the sum and we return.
    if(n == 0){
        cout << sum << endl; return;
    }
    func(n-1, sum+n);               // passing n-1, and adding the current number to the sum.
}
int main() {
    int n = 10;
    func(n,0);
    return 0;
}