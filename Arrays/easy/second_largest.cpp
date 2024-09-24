#include<bits/stdc++.h>
using namespace std;

int brute_force(vector<int> arr, int n){
  int largest = INT_MIN, s_largest = INT_MIN;
  for(int i = 0; i < n ; i++){
    largest = max(arr[i] , largest);
  }
  sort(arr.begin(),arr.end());
  for(int i = n -2 ; i >= 0; i--){
    if(arr[i] != largest){
      s_largest = arr[i];
      break;
    }
  }
  return s_largest;
}
int better(vector<int> arr, int n){

  int largest = INT_MIN, s_largest = INT_MIN;

  for(int i = 0; i < n ; i++){
    largest = max(arr[i] , largest);
  }
  for(int i = 0; i < n; i++){
    if(arr[i] > s_largest && arr[i] != largest){
      s_largest = arr[i];
    }
  }
  return s_largest;
}


int optimal(vector<int> arr, int n){ //TODO: this uses two pointer method. largest and s_largest are the two pointers here.
  int largest = INT_MIN, s_largest = INT_MIN;
  for(int i = 0 ; i < n;i++){
    if(arr[i] > largest){ //NOTE: if any element is greater than the largest, then we first set the s_largest to previous largest element.
      s_largest = largest;
      largest = arr[i]; //NOTE : after that we update the largest pointer to the current element.
    }else if(arr[i] > s_largest && arr[i] != largest){ //TODO: if we found any element that is greater than s_largest and not equal to the largest then we make it the s_largest.
      s_largest = arr[i];
    }
  }
  return s_largest; // and lastly returning the s_largest.
}
int main(){
  vector<int> arr{3,5,6,3,6,34,65,20,90};
  int n = arr.size();
  cout << "This is using brute_force method : " << brute_force(arr,n)<<endl;
  cout << "this is using better method: " << better(arr,n) << endl;
  cout << "This is optimal approach : " << optimal(arr,n) << endl;

  return 0;
}
