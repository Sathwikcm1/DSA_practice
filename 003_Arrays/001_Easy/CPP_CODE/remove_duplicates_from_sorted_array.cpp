//FIXME: the question is that we have to remove the duplicates in the array.
#include<bits/stdc++.h>
using namespace std;


//TODO: brute method is simple , put all the elements into a set. which cannot contain duplicates.
int brute_force(vector<int>& arr, int n){
  set <int> st;
  for(int i = 0 ; i < n;i++){
    st.insert(arr[i]);
  }
  int k = st.size();
  int j =0;
  for(int x : st){
    arr[j++] = x;
  }
  return k; //NOTE: we are sending the size of the set, so that we can print the array elements in the main function itself.
}

int optimal(vector<int>& arr, int n){ //TODO: in this we are basically using two pointer method. first i will be pointing to zero. the loop starts from 1.
            sort(arr.begin(),arr.end());                   //TODO: and then  check if the ith and jth elements are same or not. if not same then we make arr[i] = arr[j] and then we increment i. 
  int i = 0 ;
  for(int j =1 ; j < n;j++){
    if(arr[i] != arr[j]){
      i++;
      arr[i] = arr[j];
    }
  }
  return i + 1; // same here we are return the size of the modified array.
}
int main(){
  vector<int> arr{1,3,4,1,3,4,5,6,2,5};
  int n = arr.size();
  cout << n << endl;
  int k = brute_force(arr,n);
  for(int i = 0 ; i < k;i++){
    cout << arr[i] << " ";
  }
  cout << endl;
  cout << "This is using optimal approach takes time complexity of O(N), the question given is sorted array." << endl;
  int k2= optimal(arr,n);
  for(int i =0 ; i < k2; i++){
    cout << arr[i] << " ";
  }
  cout << endl;
  return 0;
}
