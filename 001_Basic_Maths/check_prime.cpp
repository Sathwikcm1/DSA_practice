// we have to check if the given number is prime or not.
#include<bits/stdc++.h>
using namespace std;                                    //! page no : 3

#define ll long long
void brute_force(int n){                        // this takes time complexity : O(n) and space complexity : O(1).
    int cnt = 0;
    for(int i = 1; i<= n; i++){
        if(n % i == 0) cnt++;
    }
    if (cnt == 2) cout << n << " is a prime number." << endl;
    else cout << n << " is not a prime number." << endl;
}

void optimal_approach(int n){                                           
    //? this takes time complexity : O(sqrt(n)) and space complexity : O(1).
    cout << "This is the optmal approach : " << endl;
    int cnt= 0;
    for(int i = 1; i*i < n; i++){
        if(n%i == 0){
            cnt++;
        if(n/i != i) cnt++;
        }
    }
    if(cnt == 2) cout << n << " is a prime number." << endl;
    else cout << n << " is not a prime number." << endl;
}

int main() {
    int n = 21;
    brute_force(n);
    cout << "\n";
    optimal_approach(n);
    return 0;
}