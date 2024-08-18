//! Question : 
//! Given an integer n, find the square root of n. If n is not a perfect square, then return the floor value.

//! Floor value of any number is the greatest Integer which is less than or equal to that number

// !Examples:

// !Input: n = 5
// !Output: 2
// !Explanation: Since, 5 is not a perfect square, floor of square_root of 5 is 2.
// !Input: n = 4
// !Output: 2
// !Explanation: Since, 4 is a perfect square, so its square root is 2.


#include<bits/stdc++.h>
using namespace std;
#define ll long long                                    //! page no: 103.

int brute_force_approach(int n){
    return floor(sqrt(n));         // time complexity : O(sqrt(n)) and space complexity : O(1). this is using the built-in function floor() and sqrt().
}

int better_approach(int n){     // time complexity : O(n) and space complexity : O(1).
    int ans = 1;                //? because the least value of square root is 1.
    for(int i = 1; i < n; i++) {        //? we are looping from 1 to n.
        if(i * i <= n){                 //? if i*i is less than or equal to n, then we update the ans.
            ans = i;
        }else{                          //? if not then we break the loop because we have found the ans. once we come to know the current value is greater than n, we break the loop.
            break;
        }
    }
    return ans;                         //? return the ans.
}

int optimal_approach(int n){            //todo : time complexity : O(log(n)) and space complexity : O(1). using binary search.
    int low = 1, high = n;              //todo : low is 1 because we know that the square root of 1 is 1. high is n because we know that the square root of n is n.
    while(low<=high){       
        ll mid = (low+high)/2;          //todo: long long is used to avoid overflow.
        ll val = (mid * mid);           //todo: calculating the value of mid*mid. if it is greater than n , then we need to increase the value of low to mid+1.
        if(val <= n) low = mid + 1;
        else high = mid - 1;            //todo: otherwise if it is not greater than n, then we need to decrease the value of high to mid-1. so that we can get the next value.
    }
    return high;                        //todo: high will be pointing to the square root of n. because high started from n and went down to 1.
}
int main() {
    int n = 35;
    cout << "This is using brute force approach: \n";
    cout << brute_force_approach(n);
    cout << endl;
    cout <<"This is better approach :\n";
    cout << better_approach(n) << endl;
    cout << "This is using optimal approach: \n";
    cout << optimal_approach(n) << endl;
    return 0;
}