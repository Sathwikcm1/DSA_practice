// basically picks an element and places it in the right position.
// time complexity : O(n^2) and space complexity : O(1).

#include<bits/stdc++.h>
using namespace std;

#define ll long long

void insertion_sort(int arr[], int n){          // what are we doing here : we are inserting the element in the right position.
    for(int i = 0; i < n; i++){                 // we start from the 0th index.
        int j = i;                              // j will be the index of the element we are inserting.
        while(j > 0 && arr[j] < arr[j-1]){          // if the element is smaller than the previous element, then we swap them.
            swap(arr[j],arr[j-1]);
            j--;                                // so we decrease the j by 1.
        }
    }
}
int main() {
    int arr[] = {5,3,3,6,2,8,1};
    int n = 7;
    insertion_sort(arr,n);
    return 0;
}