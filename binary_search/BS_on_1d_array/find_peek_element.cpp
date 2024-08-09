//! in this question we have to find the peek element, which means we have to find an element such that: arr[i] > arr[i-1] and also arr[i] > arr[i+1]. there may be more than one present in one array. but we need to find it.
//! for this example : arr{1,2,3,4,5,6,7,8,5,1} the answer is 8. and also consider the array starts from -infinity and ends at also -infinity. we have to return the peak index.
#include<bits/stdc++.h>
using namespace std;
#define ll long long

int brute_force_approach(vector<int> arr, int n){
    for(int i = 0; i < n; i++) {
        if((i == 0 || arr[i] > arr[i-1] )&& (i == n-1 || arr[i] > arr[i+1])) {
            return arr[i];
        }
    }
    return -1;
}

int optimized_approach(vector<int> arr, int n){         //? this one returns the peek element index.
    if(n == 1) return 0;                                //? if the array has only one element return it.
    if(arr[0] > arr[1]) return 0;                       //? if the first last element is greater than last second element then that is also a peek element return the index.
    if(arr[n-1] > arr[n - 2]) return n- 1;

    int low = 1, high = n- 2;                           //? reducing the search space because for 1st and last element has already been checked in the above two if conditions.
    while(low <= high){
        int mid = (low+high)/2;
        if(arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]) return mid;      //? if the mid element is greater than it's preceding and succeeding element then we return the mid element.
        if(arr[mid] > arr[mid - 1]) low = mid + 1; //? otherwise if it is in increase curve which the peak will never come in the left half, so we increase the low to mid + 1.
        else high = mid - 1;                        //? this is otherwise if it is in the decrease curve.
    }           
    return -1;                                      //? fake ass return statement because the func is int.
}

int main() {
    vector<int> arr{1,2,3,4,5,6,7,8,5,1}; 
    int n = arr.size();
    cout << brute_force_approach(arr,n); cout << endl;
    cout << optimized_approach(arr,n) ; cout << endl;           //todo this is returning the index of the peek element. not the element itself.
    return 0;           // something
}