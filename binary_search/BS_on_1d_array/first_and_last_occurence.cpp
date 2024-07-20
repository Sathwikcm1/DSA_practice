//! in this problem we have to find the first and last occurrence of an element in a sorted array.
#include<bits/stdc++.h>
using namespace std;
#define ll long long

vector<int> brute_force(vector<int> arr, int n , int x) {  // this takes a time complexity of O(n) and space complexity of O(1).
    sort(arr.begin(), arr.end());   // first sort the array this alone takes the time complexity of O(nlogn).
    int first = -1, last = -1;      // we got the first and last occurrence of the element in the sorted array.

    for(int i = 0; i < n; i++) {        // for loop for looping through the array.
        if(arr[i] == x){                // if we found the target, and first is still -1 then we update the first with the current index and then we update last with the current index.
            if(first == -1) first = i;  // well if first is not equal to -1, then we directly update the last with the current index.
            last  = i;
        }
    }
    return {first, last};               // and then we return a vector with the first and last index.
}

int main() {
    vector<int> arr{5, 7, 7, 8, 8, 10};
    int n = arr.size();
    int x = 8;
    vector<int> ans = brute_force(arr,n,x);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}