//FIXME: so this is the infamous two sum problem in arrays: we just have to return the sum of two numbers which is equal to the given target.
#include<bits/stdc++.h>
using namespace std;

//TODO : this is the brute one. we are just looping and adding elements in to a temp vector whose sum is equal to target.
vector<int> two_sum(vector<int> arr, int n,int target){
  vector<int> ans;
  for(int i = 0 ; i < n; i++){
    for(int j = i + 1; j < n ; j++){
      if(arr[i] + arr[j] == target){
        ans.push_back(i);
        ans.push_back(j);
        break;
      }
    }
  }
  return ans;
}

//TODO: this is using hashmap this would take O(n) time complexity over O(n^2) as in the above code.
// in this code we calculate the remaining value by subtrating each number with the target, if the value already exists in the map.
vector<int> optimised(vector<int> arr, int n, int target){
  unordered_map <int,int> mp;

  for(int i = 0 ; i < n; i++){
    int complement = target-arr[i]; //TODO: Calculating the complement, target - current element.

    //TODO: check if the complement already exists in the map, if it does that means we will get the target when we add these two numbers, 
    //so we basically have to return the i, and the complement.
    if(mp.find(complement) != mp.end()){
      return {mp[complement],i}; //TODO: return the indices found.
    }

    mp[arr[i]] = i;   //NOTE: this is adding the current number and its index to the map.
  }
  return {}; //NOTE: this is returning empty vector if no pair is found.
}
int main(){
  vector<int> arr{1,2,3,4,5,6,7,8};
  int n = arr.size();
  int target = 4;
vector<int> ans =  two_sum(arr,n,target);
  for(auto it : ans) cout << it << " ";
  cout << endl;
  cout << "This is using optimal code for two sum: " << endl;
  vector<int> res = optimised(arr,n,target);
  for(auto it: res) cout << it << " ";
  cout << endl;
  return 0;
}
