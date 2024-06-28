//! basically we have to count the number of subarrays with xor k.

#include<bits/stdc++.h>                                 //! page no : 79.
using namespace std;

#define ll long long

int brute_force(vector<int> a, int k) {             // this is the brute approach , time complexity : O(n^3) and space complexity : O(1).
    int cnt = 0;                        
    int n = a.size();                           // we have to count the number of subarrays with xor k.
    for(int i = 0; i<n;i++ ){                   // generate all possible subarrays .
        for(int j = i; j<n;j++){                
            int xorr= 0;                
            for(int k = i; k <= j;k++){         // taking the subarray and checking if the xorr is k or not , if it is k then we increment the count.
                xorr = xorr ^ a[k];
            }
            if(xorr == k){
                cnt++;
            }
        }
    }
    return cnt;                                 // and then we return the count.
}

int better_approach(vector<int> a, int k){      //? this is better approach , time complexity : O(n^2) and space complexity : O(1).
    int n = a.size();                           //? we are basically getting rid of the third for loop. that is it.
    int cnt = 0;
    for(int i = 0; i< n; i++){
        int xorr = 0;
        for(int j = i; j< n;j++){               //? so we take the subarray and check if the xorr is equal to k or not if it is equal to k then we increment the count.
            xorr = xorr^a[j];
            if(xorr == k) cnt++;               //? if the xorr is equal to k then we increment the count.
        }
    }
    return cnt;
}

int optimal_approach(vector<int> a, int k){     //todo time complexity is O(n) or can also be O(n*logn) and space complexity is O(n).
    int n = a.size();
    int xr = 0;
    map<int,int> mp;
    mp[xr]++;               //todo initialize the map with (0,1).
    int cnt = 0;            
    for(int i = 0; i<n;i++){        //todo we are just looping through the array here.
        xr = xr^a[i];               //todo calculating the xorr.
        int x = xr^k;               //todo calculating the x value to compare.
        if(mp.find(x) != mp.end()){     //todo checking if we do have x in the map or not., if we do then we increment the count.
            cnt += mp[x];
        }
        mp[xr]++;                   //todo incrementing the map based on the xorr values.
    }
    return cnt;                     //todo returning the count.
}
int main() {
    vector<int> a = {4, 2, 2, 6, 4};
    int k = 6;
    int ans = brute_force(a, k);
    cout << "The number of subarrays with XOR k is: " << ans << "\n";
    int ans2 = better_approach(a, k);
    cout << "The number of subarrays with XOR k using better apporoach is: " << ans2 << "\n";
    int ans3 = optimal_approach(a, k);
    cout << "The number of subarrays with XOR k using optimal apporoach is: " << ans3 << "\n";
    return 0;
}