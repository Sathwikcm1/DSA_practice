// basically given a number , the  output should be the number of digits in that number.
#include<bits/stdc++.h>             //! page no : 2
using namespace std;

#define ll long long
                                // time complexity : O(log10N + 1) .
int brute_approach(int n){      // we are basically counting the number of digits in the number.
    int cnt = 0;

    while(n > 0){       // loop runs until the number becomes 0.
        cnt += 1;       // this is the number of digits in the number, increasing count everytime the loop runs.
        n /=10;         // the number gets divided by 10 since it is int, the last digit is lost everytime the loop runs.
    }
    return cnt;         // at the end we return the cnt;
}

int optimal_approach(int n){                // this is the optimal approach for finding the number of digits in the number., time complexity: O(1)as simple arithmetic operations in constant time are computed on integers.
    return(int(log10(n)+1));
}


int main() {
    int n = 233434;

    cout << brute_approach(n) << endl;
    cout << "This is usin the optimal approach : " << endl;
    cout << optimal_approach(n) << endl;
    return 0;
}