//! So the question is simple: we have to find the minimum in rotated sorted array. for the optimal way we can use binary search.
#include<bits/stdc++.h>
using namespace std;                        //! page no : 96.
#define ll long long

int brute_force_approach(vector<int> arr, int n){
    int ans = INT_MAX;
    for(int i = 0; i < n; i++) {
        ans = min(ans,arr[i]);
    }
    return ans;
}

int optimal_approach(vector<int> arr, int n){ //todo This uses TC of O(log n) and SC of O(1).
    int low = 0, high = n-1;
    int ans = INT_MAX;
    while(low <= high){
        int mid = (low+high)/2;
        if(arr[low] <= arr[mid]){
            //? this means that the left half is sorted.
            ans = min(ans,arr[low]);  //? selecting the answer if it is lesser than the ans.
            low = mid + 1;              //? and then we are moving the low = mid + 1, so that we can compare the right half.
        }else{
            high = mid - 1;             //? here we are doing the same thing as before, but with the right half.
            ans = min(ans,arr[high]);
        }
    }
    return ans;
}

int main() {
    vector<int> arr{7,8,1,2,3,4,5,6};
    int n = arr.size();
    cout << "This is using brute force approach : \n";
    cout << brute_force_approach(arr,n); cout << endl;
    cout << "This is using optimal approach: \n";
    cout << optimal_approach(arr,n); cout << endl;
    return 0;
}