//FIXME: this is the same question but we have to rotate the array to the right by k places.
#include<bits/stdc++.h>
using namespace std;
void brute(vector<int>& arr,int k, int n){ // this is the brute solution for this. 
  vector<int> temp(k);
  k = k % n; // this will handle the case when the k value is greater than the size of the array.
  if( k > n) return;
  for(int i = 0; i < k ; i++) temp[i] = arr[i];
  //TODO: just copied the frontal elements , now we have to move all the elements from kth position to the 0th position.
  for(int i = 0; i < n  - k; i++) {
    arr[i] = arr[i + k];
  } //TODO: just moved the elements from the kth position to the 0th position.
  for(int i = n - k; i < n; i++){
    arr[i] = temp[i - (n - k)];
  } // TODO: in the above lines we are basically copying the first elements to the original array.
}
void reverse(vector<int>& arr, int start, int end)
{
  while (start <= end)
  {
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start++;
    end--;
  }
}
//NOTE: the above function is the function to rotate the given array.
void optimal(vector<int> arr, int k, int n){ // time complexity: O(n).
  reverse(arr, 0 , n - k - 1); // TODO : rotate the array till the kth place.
  reverse(arr, n - k, n - 1); //TODO: rotate the rest of the array from the kth place to the end of the array.
  reverse(arr, 0 , n - 1); //TODO: then reverse the whole array. which will give our answer.

}

int main(){
  vector<int> arr{1,2,3,4,5,6};
  int n = arr.size();
  int k = 2;
  cout << "Before rotating the array by k places : " << endl;
  for(int i = 0 ; i < n; i++) cout << arr[i] <<" ";
  cout << endl;
  brute(arr,k,n);
  cout << "After rotating the array to the left by k places: " << endl;
  for(int i = 0 ; i < n; i++) cout << arr[i] << " ";
  cout << endl;
  optimal(arr,k,n);
  cout << "After rotating the array by optimal method: " << endl;
  for(int i = 0  ;i < n ; i++) cout << arr[i] << " ";
  cout << endl;
  return 0;
}
