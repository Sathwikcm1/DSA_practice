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
//NOTE: The above brute force apporach willt take O(N) time complexity.



//TODO: another method is to use hashmap, whichever  values has zero at the end return it. simple!
int using_hash(vector<int> arr, int n){
  vector<int> hash(n+1,0); //NOTE: created a hash array. not a unordered_map or anything , just an array.
  //NOTE: it is n+1, because it is hash array, it contains elements from 1 to N. so it is given N+1.
  for(int i = 0 ; i < n -1; i++) hash[arr[i]]++;
  //TODO: the above line is like, for arr[i] it is doing the particular number count ++.
  for(int i = 1; i <= n; i++){
    if(hash[i] == 0){
      return i;
    }
  }
  return -1;
}



//TODO: Optimal method is to use sum formula to calucalate the sum of n numbers. and then delete the sum by that was given by the for loop.
int optimal(vector<int>arr , int n){
  int sum = (n * (n+1))/2;
  int sum2 = 0;
  for(int i = 0 ; i < n-1; i++) //size is less because one element is missing.
  {
    sum2 += arr[i];
  }
  int res = sum-sum2;
  return res;
}



int main(){

  vector<int> arr{1,2,3,4,5,6,8,9};
  int n = arr.size();
  int ans1 = brute(arr,n);
  if(ans1 != -1) cout << "The missing number in the array is " << ans1 << " ." << endl;
  else cout <<"There was no missing number in the array." << endl;

  cout << "This is using hash maps. " << endl;
  int ans2 = using_hash(arr,n);
  if(ans2 != -1) cout << "The missing element is : " << ans2 << " ." << endl;
  else cout << "there is no missing element in the given array." << endl;

  cout << "This is using Optimal way. " << endl;
  int ans3 = optimal(arr,n);
  if(ans3 != -1) cout << "The missing number is " << ans3 << "." << endl;
  return 0;
}
