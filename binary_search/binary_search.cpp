// we are basically searching in a sorted array. we find if the given number is present in the array or not. we divide the array into two parts and check if the number is present in the array or not. and then keep on doing it.

#include<bits/stdc++.h>
using namespace std;


int binary_search(vector<int> arr, int n, int target){
    int low = 0;
    int high = n-1;
    
    while(low <= high){
        int mid = (low+high)/2;
        if(arr[mid] == target) return mid;
        else if(target > arr[mid]) low = mid+1;
        else high = mid-1; 
    }
    return -1;
}
int main() {
vector<int> arr{1,2,3,4,5,6,7,8,9,10};
int n = arr.size();
if(binary_search(arr, n, 4) != -1){
    cout << "at " << binary_search(arr, n, 4)+1 << endl;
}else cout << "not found" << endl;
return 0;
}