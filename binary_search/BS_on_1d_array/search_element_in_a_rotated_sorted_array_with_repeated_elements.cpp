//! this is the same question as before, but this time the duplicates are allowed in the array. for example : 7 8 1 2 3 3 3 4 5 6
//! but the question is little bit different instead of returning the index of the target, we return if the element is present or not in the array.

#include<bits/stdc++.h>                                                 //! page no : 94.
using namespace std;
#define ll long long

bool brute_force_approach(vector<int> arr, int n, int target){
    for(int i = 0 ; i< n ; i++){
        if(arr[i] == target)
        return true;
    }
    return false;
}

bool optimal_approach(vector<int> arr, int target, int n){ //todo And obviosly the time complexity of this is O(log n) and SC is O(1).
    int low = 0, high = n-1;
    while(low <= high){
        int mid = low + (high - low) / 2;
        if(arr[mid] == target) return true;
        if (arr[low] == arr[mid] && arr[mid] == arr[high]){ //? this part is to handle the duplicates. if the low and mid and the high is found to be the same, then we reduce the range by 1.
            low++;
            high--;
            continue; //? continue is because we are still not sure if the target is present or not. so we continue the loop.
        }
        if(arr[low] < arr[mid]){
            //? this means the left part of the array is sorted.
            if(arr[low] <= target && target < arr[mid]){
                high = mid - 1;
            }else{
                low = mid + 1;
            }
        }
        else{
            if(arr[mid] < target && target <= arr[high]){
                                        //? this means the right part of the array is sorted.
                low = mid + 1;
                }
                else{
                    high = mid - 1;
                }
        }
    }
    return false;
}


int main() {
    vector<int> arr{7, 8, 1, 2, 3, 3, 3, 4, 5, 6};
    int n = arr.size();
    int target = 3;
    cout << "This is using brute force approach  :\n";
    if(brute_force_approach(arr,n,target)) cout << "The element is present in the array\n";
    else cout << "The element is not present in the array.\n";
    cout << "This is using optimal approach : \n";
    if(optimal_approach(arr,target,n)) cout << "The element is present in the array\n";
    else cout << "The element is not present in the array.\n";
    return 0;
}