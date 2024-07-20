//! in this problem we have to find the first and last occurrence of an element in a sorted array.
#include<bits/stdc++.h>
using namespace std;
#define ll long long

int lower_bound_z(vector<int> arr, int n , int target){   
    int low = 0; int high = n-1;  int ans = n;
    while (low <= high)
    {
        int mid = (high+low)/2;
        if(arr[mid] >= target) {
            ans = mid;
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }
    
    return ans;
}

int upper_bound_z(vector<int> arr, int n , int target){
    int low=  0, high  = n-1 , ans = n;
    while(low <= high){
        int mid = (high+low)/2;
        if(arr[mid] > target){
            ans = mid;
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }
    return ans;
}

vector<int> brute_force(vector<int> arr, int n , int x) {  // this takes a time complexity of O(n) and space complexity of O(1).
    sort(arr.begin(), arr.end());   // first sort the array this alone takes the time complexity of O(nlogn).
    int first = -1, last = -1;      // we got the first and last occurrence of the element in the sorted array.

    for(int i = 0; i < n; i++) {        // for loop for looping through the array.
        if(arr[i] == x){                // if we found the target, and first is still -1 then we update the first with the current index and then we update last with the current index.
            if(first == -1) first = i;  // well if first is not equal to -1, then we directly update the last with the current index.
            last  = i;
        }
    }
    return {first, last};               // and then we return a vector with the first and last index.
}

vector<int> better_approach(vector<int> arr, int n , int target){ //? this takes a time complexity of 2* O(log n) and space complexity of O(1).
    int lb = lower_bound_z(arr, n, target);                     //? in this approach we are using the lower_bound function to find the first occurrence of the target in the array.
    if(lb == n || arr[lb] != target) return {-1, -1};           //? if the lb == b, which means that the target is not found in the array, or the lb is not equal to the target then we return {-1, -1}.
    return {lb , upper_bound_z(arr, n , target) - 1};           //? otherwise we return a vector or a pair with the lb and up - 1.
}

int first_occurrence(vector<int> arr, int n , int k){ //todo: i don't how this is better than the better approach but hear me out.
    int first = -1, high = n-1, low = 0;
    while(low <= high){             
        int mid = (high+low)/2; 
        if(arr[mid] == k){
            first = mid;                                    //todo if you find the element, we update the first with the current index.
            high = mid -1;                                  //todo then we update the high to mid - 1 because the element is definitely not in the right half of the array since we are trying to find the first occurrence.
        }else if(arr[mid] < k) low = mid + 1;               //todo otherwise we update the low to mid + 1 because the element is definitely not in the left half of the array since we are trying to find the first occurrence.
        else high = mid - 1;                                //todo otherwise we update the high to mid - 1 because the element is definitely not in the right half of the array since we are trying to find the first occurrence.
    }   
    return first;                                           //todo returning the first.
}

int last_occurrence(vector<int> arr, int n, int k){     //todo this is the same as above.
    int low = 0, high = n-1, last = -1;
    while(low <= high){
        int mid = (low+high)/2;
        if(arr[mid] == k){
            last = mid;
            low = mid + 1;
        }else if(arr[mid] < k) low = mid + 1;
        else high = mid - 1;
    }
    return last;
}

vector<int> optimal_approach (vector<int> arr, int n , int k){   //todo this is where we call the above two functions.
    int first = first_occurrence(arr, n, k);
    if (first == -1) return {-1,-1};                            //todo: if first == -1 , which means that we did not find the target in the array at all, so there is no need to check for the last occurrence , which would again save us from a lot of time and space complexity.
    int last = last_occurrence(arr, n, k);
    return {first, last};                                       //todo well if we do find the first and last, we return it back as a vector.
}

int main() {
    vector<int> arr{5, 7, 7, 8, 8, 10};
    int n = arr.size();
    int x = 8;
    sort(arr.begin(), arr.end());
    vector<int> ans = brute_force(arr,n,x);
    cout << "The is brute force approach : \n";
    cout << ans[0] << " " << ans[1] << endl; // something.
    vector<int> ans2 = better_approach(arr,n,x);
    cout << "The is better approach : \n";
    cout << ans2[0] << " " << ans2[1] << endl;
    vector<int> ans3 = optimal_approach(arr,n,x);
    cout << "The is optimal approach : \n";
    cout << ans3[0] << " " << ans3[1] << endl;
    return 0;
<<<<<<< HEAD
}
=======
} // mew
>>>>>>> 348efe172ec2f3622d389a9da95b3fe526ae4362
