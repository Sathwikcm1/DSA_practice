#include<bits/stdc++.h>
using namespace std;
#define ll long long

int brute_approach(vector<int> arr, int n, int x) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            count++;
        }
    }
    return count;
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
int count(vector<int> arr, int n, int x) {
    vector<int> ans = optimal_approach(arr, n, x);
    if (ans[1] == -1) return 0;
    return ans[1] - ans[0] + 1;                                       //todo checkout the logic here, because the array is sorted, we can just return the difference between the last index and the first index + 1.
}

int main() {
    vector<int> arr{5, 7, 7, 8, 8, 10};
    int n = arr.size();
    int x = 8;
    cout << brute_approach(arr,n,x) << endl;
    cout << "This is optimal approach , this uses O(log n) because of binary search rather than linear search: that costs O(n). \n";
    optimal_approach(arr,n,x);
    return 0;
}