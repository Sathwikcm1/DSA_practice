//! This question is basically about finding the minimum days required to make "m" no of boquets of "k" no of roses.
//! provided that the ith rose will be bloomed in the ith day. 
/*! Sample Input 1 :
9
1 2 1 2 7 2 2 3 1
3 2
Sample Output 1 :
3
Explanation For Sample Input 1 :
We will return 3, because:
All the roses with 'arr[i]' less than equal to 3 have already bloomed after 3 days, this means every rose except the 5th rose has bloomed. Now we can form the first bouquet from the first three roses and the second bouquet from the last three roses.
 !*/

#include<bits/stdc++.h>
using namespace std;
#define ll long long

bool possible(vector<int> arr, int day, int k, int m){      //? this is required for both brute and optimal approach., this is basically asking if the chosen day is possible or not.
    int cnt = 0, no_of_boq = 0;                             //? no of boq is the number of boquets made on the chosen day. cnt is the number of roses bloomed on the chosen day.
    for(int i = 0 ; i < arr.size(); i++){                   //? for loop goes through the array.
        if(arr[i] <= day)   cnt++;                          //? only if the current element of the array(arr[i]) is less than the day that is chose , then we do cnt++ because it passed
        else{
            no_of_boq += cnt/k;                             //? otherwise we reinitialize the cnt to 0 and count the no of boquets, cnt/k is because cnt is counting the roses not boqs.
            cnt = 0;
        }   
    }
    no_of_boq += cnt/k;                                     //? counting the no_of_boqs. what if every element passed on that moment this is required.
    if(no_of_boq >= m) return true;                         //? if the no_of_boqs meets the requirement then it is true otherwise it is false.
    else return false;
}


int brute_force_approach(vector<int> arr,int k, int m){       // this is brute approach that takes O(n * maxi - mini + 1) complexity.
    int mini = INT_MAX, maxi = INT_MIN;
    for(int i = 0 ; i < arr.size();i++){                    //calculating minimum and the maximum element in the array.
        mini = min(mini,arr[i]);
        maxi = max(maxi,arr[i]);
    }
    for(int i = mini; i < maxi; i++){                       //looping range is from minimum to maximum.
        if(possible(arr,i,m,k) == true ) return i;          // if the chosen day is possible, then we return the chosen day.
    }
    return -1;                                              // if the chosen day is not possible, then we return -1.
}

int optimal_approach(vector<int> arr, int m, int k){
    ll val = m * 1ll * k * 1ll;
    if (val > arr.size()) return -1;
    int mini = INT_MAX, maxi = INT_MIN;
    for(int i = 0 ; i < arr.size();i++){
        mini = min(mini,arr[i]);
        maxi = max(maxi,arr[i]);
    }
    int low = mini, high = maxi;
    while(low <= high){
        int mid = (low+high)/2;
        if(possible(arr,mid,m,k) == true) high = mid - 1;
        else low = mid + 1;
    }
    return low;
}


int main() {
    vector<int> arr = {7, 7, 7, 7, 13, 11, 12, 7};
    int k = 3;                                      //todo this is the number of roses.
    int m = 2;                                      //todo this is the number of boquets.
    int ans = brute_force_approach(arr, k, m);
    cout << "This is using brute force approach : \n";
    if (ans == -1)
        cout << "We cannot make m bouquets.\n";
    else
        cout << "We can make bouquets on day " << ans << "\n";
    cout << "This is using optimal approach : \n";
    cout << optimal_approach(arr, k, m) << "\n";
    return 0;
}