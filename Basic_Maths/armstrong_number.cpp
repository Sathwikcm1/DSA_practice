// basically the given number is equal to the sum of the cube of the each digit of the number itsefl ex: 371.

#include<bits/stdc++.h>
using namespace std;                //! page no : 2.

#define ll long long

int main() {
    int n = 371;
    int og = n;
    int sum = 0;            // initializing the sum.
    while(n > 0){
        int ld = n%10;
        sum = sum + (ld*ld*ld);    // multiplying the last digit 3 times and adding it to the sum.
        n/=10;
    }
    if(og == sum) cout << "The number is armstrong number \n"<<endl;
    else cout << "The number is not armstrong number.\n";
    return 0;
}