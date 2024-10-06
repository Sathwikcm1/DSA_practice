//FIXME: Union of two sorted arrays. Unions of two arrays inlcludes getting all the elements together only unique elements will present. 
#include<bits/stdc++.h>
using namespace std;


//TODO: so my first thougths for brute force is to add all the elements to a set. and then return the set.
//we can also do the same thing using map data structure, that also stores unique elements and in a ordered way. 
vector<int> brute_approach(vector<int> arr1, int n, vector<int> arr2, int m){
  map <int, int> freq;
  vector<int> ans; //NOTE: this is our answer to be returned.
  for(int i = 0 ; i < n;i++){
    freq[arr1[i]]++;
  }
  for(int i = 0 ; i < m; i++)
    freq[arr2[i]]++;
  for(auto &it : freq)
    ans.push_back(it.first);
  return ans;
}
//TODO: using sets: 
// This uses the time complexity of O( (m+ n) log(m + n)) both sets and maps.
vector<int> setss(vector<int> arr1, int n , vector<int> arr2, int m){
  set<int> st;
  for(int i = 0; i < n; i++)
    st.insert(arr1[i]);
  for(int i = 0 ;i < m;i++)
    st.insert(arr2[i]);
  vector<int> ans(st.begin(),st.end());
  return ans;
}
//TODO: this is using two pointers method.
vector<int> optimal(vector<int>arr1 , int n, vector<int> arr2, int m){
  int i = 0 , j  = 0; //NOTE: these are the pointers.
  vector<int> ans;
  while(i < n && j < m){
    if(arr1[i] <=  arr2[j]){
      if(ans.size() == 0 || ans.back() != arr1[i])
        ans.push_back(arr1[i]);             //TODO: we are adding the least element first to the array, only if the element is not already present int the arrays.
      i++;
    } else{
      if(ans.size() == 0 || ans.back() != arr2[j] )
        ans.push_back(arr2[j]);
      j++;
    } 
  }
  while( i < n) // IF any element left in the first array.
  {
    if(ans.back() != arr1[i])
      ans.push_back(arr1[i]);
    i++;
  }

  while( j < m) // IF any element left in the second array.
  {
    if(ans.back() != arr2[j])
      ans.push_back(arr2[j]);
    j++;
  }
  return ans;
}

int main(){
  vector<int> arr1 { 2, 3, 5, 7, 8, 9,10};
  vector<int> arr2 { 1,2,3,4,5,6,7,7,9,10};
  int n = arr1.size();
  int m = arr2.size();
  cout << "This is using maps: " << endl;
  vector<int> ans = brute_approach(arr1,n,arr2,m);
  for(auto it : ans) cout << it << " ";
  cout << endl;
  cout << " This is using sets. " << endl;
  vector<int> ans2 = setss(arr1,n,arr2,m);
  for(auto it: ans2) cout << it << " ";
  cout << endl;
  cout << "This is using two poionter method, less time complexity: O(N + M): " << endl;
  vector<int> ans3 = optimal(arr1,n,arr2,m);
  for(auto it: ans3) cout << it << " ";
  cout << endl;
  return 0;
}
