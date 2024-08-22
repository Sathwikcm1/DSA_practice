//!In this problem we have to find the nth root of a number.
//! example : 3rd root 27 is 3, 4th root of 69 doesn't exist so we return -1.

#include<bits/stdc++.h>
using namespace std;
#define ll long long


int func(int b, int exponent){      // this takes the base and the exponent and returns the value of the nth root //? time complexity : O(log n).
    ll ans = 1;                     // initially we set the ans to 1.
    ll base = b;                    // initially we set the base to b.
    while(exponent > 0){            // while the exponent is greater than 0
        if(exponent%2 == 1){        // if the exponent is odd then we multiply the ans with the base with decreasing the exponent by 1.
            exponent--;
            ans = ans * base;
        }else{
            exponent/=2;            // otherwise if the exponent is even then we divide the exponent by 2.
            base = base * base;     // and we multiply the base with itself.
        }
    }
    return ans;                     // and then we finally return the ans.
}
int brute_force(int n, int m){      //? time complexity : O(m * log n) and space complexity : O(1).
    for(int i = 1; i < m; i++) {    // for loop goes from 1 to m, m is the number of roots we want to find, it starts from 1 because the 1st root is 1.
        ll val = func(i,n);         // calculating the value of i^n by calling function func.
        if(val == m * 1ll) return i;    // if the value is equal to m then we return i because we have found the nth root.
        else if(val > m* 1ll) break;    // otherwise we break out of the for loop and return -1.
    }
    return -1;
}

int optimal_approach(int n, int m){         //todo This is using binary search time complexity : O(log m * log n) and space complexity : O(1).
    int low = 1, high = m;                  //todo  Again we start from low as 1 as that is lowest root, and high as m as that is the highest root because the number itself is the highest root.
    while(low <= high){
        int mid = low + (high - low)/2;
        if(func(mid, n) == m) return mid;           //todo , if the value of mid is equal to m then we return mid.
        else if(func(mid, n) < m) low = mid + 1;    //todo if the value of mid is less than a number then we increase the value of low to mid + 1.
        else high = mid - 1;                        //todo if the value of mid is greater than a number then we decrease the value of high to mid - 1.
    }
    return -1;                                      //todo fake ass return statement because the func is int.
}
int main() {
    int n = 3, m = 27;
    int ans = brute_force(n, m);
    cout << "The answer using brute approach is: " << ans << "\n";
    int ans2 = optimal_approach(n, m);
    cout << "The answer using optimal approach is : " << ans2 << "\n";

    return 0;
}