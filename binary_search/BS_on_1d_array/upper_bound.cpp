//! given an array and a number , we have to find the index of the first element which is greater than to the given number : arr[index] > target.

#include<bits/stdc++.h>
using namespace std;
#define ll long long

int upper_boundz(vector<int> arr, int n, int target){        //? we are basically searching in a sorted array. so the array must be sorted otherwise it should sorted before the algorithm starts
    int low = 0, high = n-1 ,ans = -1;                       //? answer is the index of the first element which is greater than the target
    while(low<=high){
        int mid = (low+high)/2;
        if(arr[mid] > target){                             //? we check if the mid index is less than the target or not if it is then we increase the low pointer so that we can get the next index.
            ans = mid;
            high = mid-1;
        }else{
            low = mid+1;                                    //? else we decrease the high pointer so that we can get the next index.
        }
    }
    return ans;                                             //? otherwise we return the ans.
}
int main() {
    vector<int> arr{1, 2, 2, 2, 2, 3, 3, 3, 3};
    int n = arr.size();
    int target = 2;
    cout << upper_boundz(arr,n,target) << endl;
    //todo otherwise we can just the STL function that is upper_bound(arr.begin(),arr.end(),target)
    upper_bound(arr.begin(),arr.end(),target);
    cout << upper_bound(arr.begin(),arr.end(),target) - arr.begin() << endl; //todo that extra "- arr.begin()" is used to get the index , otherwise it would have returned the iterator
    return 0;
}