// basically we have to return the length of the largest subarray with 0 sum.
// just like kadane's algorithm this is very similar to that of max sum subarray problem.
#include<bits/stdc++.h>
using namespace std;

#define ll long long

int optimal_approach(vector<int> arr, int n){       // ? time complexity is basically O(n) and space complexity is O(n).
    int sum = 0;                                      // ? so we initialize the sum to zero.
    int maxi = 0;                                      // ? so we initialize the maxi to zero.
    unordered_map <int,int> mp;                         
    for(int i = 0; i < n; i++){                                 // ? here we iterate through the array.
        sum += arr[i];                                            // ? so we calculate the sum of the array.
        if(sum == 0){                                               // ? if the sum is equal to zero then we return the length of the array.
        maxi = i+1;                                             //? calculating the length of the array.
        }else if(mp.find(sum) != mp.end()){                     //? if the sum is already present in the map then we return the length of the array.
            maxi = max(maxi, i-mp[sum]);                        //? so we subtract the index of the sum from the index of the sum in the map. (s-k) part.
        }else{                                                    //? if the sum is not present in the map then we insert the sum and its index in the map.
        mp[sum] = i;
        }
    }
    return maxi;
}

int main() {
    vector<int> arr{9, -3, 3, -1, 6, -5};
    int n = arr.size();
    int ans = optimal_approach(arr, n);
    cout << "This is using optimal approach: " << ans << endl;
    return 0;
}