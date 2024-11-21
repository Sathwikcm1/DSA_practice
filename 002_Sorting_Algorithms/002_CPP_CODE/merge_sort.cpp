// uses divide and merge concept.
// time complexity : O(nlogn) and space complexity : O(n)., one of the best time and space complexity in sort algorithm.
#include<bits/stdc++.h>
using namespace std;

#define ll long long                            //! page no : 9

void merge(vector<int>&arr, int low, int mid, int high){        // this is the merge function. this is where we merge the array.
    int left = low;                         // index for the left array. 
    int right = mid+1;                      // index for the right array.
    vector<int> temp;

    while(left <= mid && right <= high){        // a while loop  that runs till the left and right index is less than or equal to the mid and high.
        if(arr[left] < arr[right]){             // if the element from the left array is smaller than the right one , then we add that element to the temp vector and move to next element in the array.
            temp.push_back(arr[left++]);
        }else{
            temp.push_back(arr[right++]);       // same here.
        }
    }

    while(left <= mid){                         // this is for the remaining elements.
        temp.push_back(arr[left++]);
    }
    while(right <= high){
        temp.push_back(arr[right++]);
    }

    for(int i = low; i<=high; i++){             // copying the elements from the temp vector to the original array.
        arr[i] = temp[i-low];
    }
}


void merge_sort(vector<int>&arr, int low, int high){        // this is first function that is called.
    if(low>=high) return;                   // if low is greater than high, then we return.
    int mid = (low+high)/2;                 // we calculate the mid index of the current array.
    merge_sort(arr,low,mid);                // recursively calling the merge_sort function with sending the array and the low and mid index. divide the array.
    merge_sort(arr,mid+1,high);
    merge(arr,low,mid,high);                // calling the merge function with sending the array and the low, mid and high index. merge the array.
}

int main() {
    vector<int> arr{5,5,2,7,2,6,9,1,12};
    int n= arr.size();
    merge_sort(arr,0,n-1);                      // calling the merge_sort function with sending the array and the low and high index.
    // for(int i: arr) cout<< arr[i] << " ";
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
    return 0;
}