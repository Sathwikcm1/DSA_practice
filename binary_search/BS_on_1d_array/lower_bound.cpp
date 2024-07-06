//! we have to return the lowest index of the element in the array which is arr[i] >= target.
#include<bits/stdc++.h>
using namespace std;
#define ll long long

int lower_bound(vector<int> arr, int n, int target){        //? we are basically searching in a sorted array. so the array must be sorted otherwise it should sorted before the algorithm starts
    int low = 0, high = n-1 ,ans = n;                       //? answer is the size of the array because we have to return the lowest index of the element in the array which is arr[i] >= target if not found then we return the size of the array.
    while(low<=high){
        int mid = (low+high)/2;
        if(arr[mid] >= target){                             //? we check if the mid index is greater than the target or not if it is then we decrease the high pointer so that we can get the next index.
            ans = mid;
            high = mid-1;
        }else{
            low = mid+1;                                    //? else we increase the low pointer so that we can get the next index.
        }
    }
    return ans;                                             //? otherwise we return the ans.
}
int main() {
    vector<int> arr{1, 2, 2, 2, 2, 3, 3, 3, 3};
    int n = arr.size();
    int target = 2;
    cout << lower_bound(arr,n,target) << endl;
    return 0;
}