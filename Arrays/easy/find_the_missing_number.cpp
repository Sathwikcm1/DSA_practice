//FIXME: so the question is to find the missing number in an array from 1 to N, find the 
//missing number (between 1 to N), that is not present in the array.
#include<bits/stdc++.h>
using namespace std;

//TODO: first thing that poped to my mind is to check if there is any one of i is missing in the loop.
int brute(vector<int> arr, int n){
  sort(arr.begin(),arr.end());
  for(int i = 1 ; i < n; i++){
    if (i != arr[i-1]) return i;
  }
  return -1;
}
int main(){

  vector<int> arr{1,2,3,4,5,6,8,9};
  int n = arr.size();
  int ans1 = brute(arr,n);
  if(ans1 != -1) cout << "The missing number in the array is " << ans1 << " ." << endl;
  else cout <<"There was no missing number in the array." << endl;
  return 0;
}
