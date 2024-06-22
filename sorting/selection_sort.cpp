// selecting the minimum element and putting it in order.  
#include<bits/stdc++.h>                             //! page no : 6
using namespace std;

#define ll long long                        // time complexity : O(n^2)
void selection_sort(int arr[],int n){// we take the smallest element in the array and place it in the beginning.

    int mini;                       // minimum index for the array remaining.
    for (int i = 0; i < n-1; i++)   // no need to sort the last element becuase it will already be sorted.
    {   mini =i;
        for(int j = i+1; j<n; j++){     // so we start from i+1 till n
            if(arr[j] < arr[mini])
                mini = j;        
                }
            swap(arr[i],arr[mini]);
    }
    
}

int main() {
    int arr[]={5,3,3,6,2,8,1};
    selection_sort(arr,7);
    cout << "The array after sorting: \n";
    for(int i = 0; i< 7;i++){
        cout << arr[i] << " ";
    }
        return 0;
}