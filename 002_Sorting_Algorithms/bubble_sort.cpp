// bubbles up the largest element in the array to the end of the array.
#include<bits/stdc++.h>
using namespace std;            //!page no : 8.

#define ll long long

void bubble_sort(int arr[],int n){            // time complexity : O(n^2) and space complexity : O(1).
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n-i-1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j],arr[j+1]);
            }
        }
    }
    cout << "This is using bubble sort: \n";
    for(int i = 0; i<n;i++){
        cout << arr[i] << " ";
    }
}
int main() {
    int arr[]={5,3,3,6,2,8,1};
    int n = 7;
    bubble_sort(arr,n);
    return 0;
}
