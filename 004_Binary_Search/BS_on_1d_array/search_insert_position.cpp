//! we have to return the index where the element should be inserted in the array.

#include<bits/stdc++.h>
using namespace std;
#define ll long long

int search_insert(vector<int> arr, int n, int target) {         //todo : this is basically lower_bound problem.
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
    return ans;    
}
int main() {
    // int x = 5;
    vector<int> arr{1, 3, 5, 6};
    int n = arr.size();
    int target = 2;
    cout << search_insert(arr, n, target);
    return 0;
}