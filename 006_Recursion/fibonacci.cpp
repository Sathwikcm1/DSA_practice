// we are printing fibonacci numbers till the given n, here we are using recursion.
#include<bits/stdc++.h>
using namespace std;

#define ll long long

int fibonacci(int n){
    if(n<=1) return n;
    return fibonacci(n-1)+fibonacci(n-2);
}

int main() {
    int n = 7;
    cout << fibonacci(n) << endl;
    return 0;
}