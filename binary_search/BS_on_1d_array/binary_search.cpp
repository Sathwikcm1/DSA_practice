// we are basically searching in a sorted array. we find if the given number is present in the array or not. we divide the array into two parts and check if the number is present in the array or not. and then keep on doing it.

#include<bits/stdc++.h>
using namespace std;


int binary_searchs(vector<int> arr, int n, int target){      //? we are basically searching in a sorted array. so the array must be sorted otherwise it should sorted before the algorithm starts
    int low = 0;                                            //? this is low pointer pointing to the first element of the array
    int high = n-1;                                         //? this is the high pointer pointing to the last element of the array.
    
    while(low <= high){                                     //? this should run till the low pointer crosses the high pointer
        int mid = (low+high)/2;                             //? calculating the mid index 
        if(arr[mid] == target) return mid;                  //? checking if the mid index is equal to the target, if it is then we return the index.
        else if(target > arr[mid]) low = mid+1;             //? if the target is greater than the mid index, then we increase the low pointer so that we can get the next index.
        else high = mid-1;                                  //? else we decrease the high pointer so that we can get the next index.
    }
    return -1;                                              //? otherwise we return -1 indicating 
}
int main() {
vector<int> arr{1,2,3,4,5,6,7,8,9,10};
int n = arr.size();
if(binary_searchs(arr, n, 4) != -1){
    cout << "at " << binary_searchs(arr, n, 4)+1 << endl;
}else cout << "not found" << endl;
bool mew = binary_search(arr.begin(), arr.end(), 4);
cout << mew;
cout << endl;
return 0;
}