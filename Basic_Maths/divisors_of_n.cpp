// basically we have to print all the divisors of the given number.
#include<bits/stdc++.h>
using namespace std;                                    //! page no : 3.

#define ll long long
void optimal_approach(int n){                   //? this is the optimal approach, time complexity : O(sqrt(n)) and space complexity : O(1)
    for(int i = 1; i*i < n; i++){               //? we are basically looping till the square root of the number. because we know that it's factors comes within the square root of the number.
        if(n%i == 0){cout << i << " ";
        if(i != n/i) cout << n/i << " ";        //? if i is not equal to the number divided by i, then we print the number divided by i.
    }
}
}

void brute_force_approach(int n){                       // time complexity : O(n), space complexity : O(1).
    cout << "This is brute force approach : " << endl;
    for(int i = 1; i <= n; i++){                       // we are looping from 1 to n.
        if(n%i == 0) cout << i << " ";
    }                                                       // and printing all the divisors.
}

int main() {
    int n = 10;
    optimal_approach(n);
    cout << "\n";
    brute_force_approach(n);
    return 0;
}