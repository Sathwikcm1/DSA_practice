//! So the question is simple: we have to find the minimum in rotated sorted array. for the optimal way we can use binary search.
//! i know this is the previous question but in order to find how many times an array has been rotated we just need to find the index of the minimum element.
#include<bits/stdc++.h>
using namespace std;                        //! page no : 96.
#define ll long long

// int brute_force_approach(vector<int> arr, int n){ redundant code
//     int ans = INT_MAX;
//     for(int i = 0; i < n; i++) {
//         ans = min(ans,arr[i]);
//     }
//     return ans;
// }

int optimal_approach(vector<int> arr, int n){ //todo This uses TC of O(log n) and SC of O(1).
    int low = 0, high = n-1;
    int ans = INT_MAX;
    int index = -1;
    while(low <= high){
        int mid = (low+high)/2;
        if(arr[low] <= arr[high]) {  //? this is for the case when the array is already sorted.
            if(arr[low] <= ans){
                index = low;
                ans = arr[low];
            }break; //? this where we put break, to break the loop because the array is already sorted.
        }
        if(arr[low] <= arr[mid]){       //? this is the part where the left part is sorted.
            if(arr[low] <= ans){        //? if the arr[low] is less than the answer we already have we change the ans to a[low] otherwise we just update the low = mid + 1.
                index = low;            //todo this is exactly where we update the index of the minimum which we need to return.
                ans = arr[low];
            }
            low = mid + 1;
        }else{
            high = mid - 1;
            if(arr[mid] <= ans){
                index = mid;
                ans = arr[mid];
            }
        }
    }
    return index;
}

int main() {
    vector<int> arr{7,8,1,2,3,4,5,6};
    int n = arr.size();
    // cout << "This is using brute force approach : \n";
    // cout << brute_force_approach(arr,n); cout << endl;
    // cout << "This is using optimal approach: \n";
    cout << "The Array has been rotated " << optimal_approach(arr,n) << " times.\n";
    // cout << optimal_approach(arr,n); cout << endl;
    return 0;
}
