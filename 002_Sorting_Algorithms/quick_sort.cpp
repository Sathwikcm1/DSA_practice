// we pick a pivot element and place it in the right position., and then we sort the left and right subarrays.
// time complexity also takes O(nlogn) and space complexity : O(1).
#include<bits/stdc++.h>
using namespace std;

#define ll long long
int partition(vector<int> &arr, int low, int high){
    int pivot = arr[low];
    int i = low;
    int j= high;
    while(i < j){
        while(arr[i] <= pivot && i < high) i++;
        while(arr[j] > pivot && j > low) j--;
        if(i < j) swap(arr[i],arr[j]);
    }
    swap(arr[low],arr[j]);
    return j;
}

void quick_sort(vector<int> &arr, int low, int high){
    if(low >= high) return;
    int P_index = partition(arr,low,high);
    quick_sort(arr,low,P_index-1);
    quick_sort(arr,P_index+1,high);
}

int main() {
    vector<int> arr{5,5,2,7,2,6,9,1,12};
    int n = arr.size();
    quick_sort(arr,0,n-1);
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
    return 0;
}