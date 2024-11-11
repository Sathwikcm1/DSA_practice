#include<bits/stdc++.h>
using namespace std;
                        // we are basically printing n to 1 using recursion.
#define ll long long        //! page no : 25.


void func(int n){
    if(n == 0) return;
    cout << n << endl;
    func(n-1);
}
int main() {
    int n = 17;
    func(n);
    return 0;
}