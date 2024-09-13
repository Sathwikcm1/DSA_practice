#include<bits/stdc++.h>
using namespace std;
#define ll long long



int maxinarr(vector<int> arr, int  n){
    int ans = -1;
    for(int i = 0 ; i < n;i++) ans = max(ans,arr[i]);
    return ans;
}

int func(vector<int> arr, int hours){
    int n = arr.size();
    int totalhr = 0;
    for(int i = 0; i < n; i++){
        totalhr += ceil((double)arr[i]/hours);
    }
    return totalhr;
}

int minimumRateToEatBananas(vector<int> arr, int h) {
    // Write Your Code Here
    int n = arr.size();
    for(int i = 1; i < maxinarr(arr,n); i++){
        int reqtime = func(arr, i);
        if( reqtime <= h) return i;
    }
    return -1;
}


//? optimal approach : 

int findMax(vector<int> &v) {
    int maxi = INT_MIN;
    int n = v.size();
    //find the maximum:
    for (int i = 0; i < n; i++) {
        maxi = max(maxi, v[i]);
    }
    return maxi;
}

int calculateTotalHours(vector<int> &v, int hourly) {
    int totalH = 0;
    int n = v.size();
    //find total hours:
    for (int i = 0; i < n; i++) {
        totalH += ceil((double)(v[i]) / (double)(hourly));
    }
    return totalH;
}

int minimumRateToEatBananasoptimal(vector<int> v, int h) {
    int low = 1, high = findMax(v);

    //apply binary search:
    while (low <= high) {
        int mid = (low + high) / 2;
        int totalH = calculateTotalHours(v, mid);
        if (totalH <= h) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    return low;
}

int main() {
    vector<int>  piles = {3,6,7,11};
    int h = 8;
    cout << "This is the brute force approach : " << endl;
    cout << minimumRateToEatBananas(piles,h); 
    cout << endl;
    cout << "This is using the otpmal approach : " << endl;
    cout << minimumRateToEatBananasoptimal(piles,h);
    cout << endl;
    return 0;
}