//! so the problem is that we have to find (myself) single element in the array where every other element has appeared more than once.

#include<bits/stdc++.h>
using namespace std;
#define ll long long                                //! page no : 97.


int brute_force(vector<int> arr, int n){                    // time complexity ; O(n)
    if(n == 1) return arr[0]; // because the array has only one element.
    for(int i = 0; i < n; i++) { // for loop to go through the array.
        if(i == 0) {                                    // if the element is the first element in the array.
            if(arr[i] != arr[i+1]) return arr[i];        // we only check if the next element is same as the current element or not. if it is not then we return the current element. 
        }else if(i == n-1){                             // checking for the last element of the array.
            if(arr[i] != arr[i-1]) return arr[i];       // we check if the previous element to the current element is same as the current element if not we return the current element.
        }else{
            if(arr[i] != arr[i-1] && arr[i] != arr[i+1]) return arr[i]; // this is for every other element in the array. we check for both sides of the element.
        }
    }
    return -1;                              // just return -1 if we don't find any single element in the array.
}

int optimal_approach(vector<int> arr, int n){   //? this is using binary search takes time complexity of O(log n).
    if (n == 1) return arr[0];                  //? if the array has only one element then we return that element.
    int low = 1, high = n-2;                    //? reducing the search space by 1 for binary search.
    if(arr[0] != arr[1]) return arr[0];         //? if the first element is not equal to the second element then we return the first element.
    if(arr[n-1] != arr[n-2]) return arr[n-1];   //? doing the same for the last element of the array.

    while(low <= high){
        int mid = (low + high) / 2;
        if(arr[mid] != arr[mid-1] && arr[mid] != arr[mid+1]) return arr[mid];       //? return the mid element if it is not equal to the previous and next element.

        if(mid % 2 == 1 && arr[mid] == arr[mid - 1] || mid % 2 == 0 && arr[mid] == arr[mid + 1]){ //? checking if the mid element is odd or even and then check if the mid and mid - 1 or mid and mid + 1 is same or not if it is same then we eliminate the left half of the array.
            low = mid + 1;
        }else{                                          //? opposite of the above code.
            high = mid - 1;
        }
    }
    return -1;              //? default return -1 if we don't find any single element in the array.
}
int main() {
    vector<int> arr{1, 1, 2, 3, 3, 4, 4, 8, 8};
    int n = arr.size();
    cout << "This is using brute force approach : \n" << brute_force(arr,n);
    cout << endl;
    cout << "This is using optimal approach: \n" << optimal_approach(arr,n);
    cout << endl;
    return 0;
}