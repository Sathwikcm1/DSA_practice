//FIXME: the question is to move all the zeroes present in the array to last places of the array.
#include<bits/stdc++.h>
using namespace std;

void brute(vector<int> &arr, int n){ //TODO: this is the brute force approach it takes o(2N).
  vector<int> temp;
  for(int i = 0; i < n ; i++){ //TODO: we are copying all the non zeroe elements here to a temporary array.
    if(arr[i] != 0){
      temp.push_back(arr[i]);
    }
  } //TODO:  we take the size of the non zero elements array. 
    int ts= temp.size();
  for(int i = 0 ; i < ts; i++){
    arr[i] = temp[i];
  } //NOTE: we are  copying the temp array to the original array till the size of the temporary array.
    //TODO:  we are making the remaining elements as zeroes.
  for(int i = ts; i < n; i++) arr[i] = 0;
 cout << "After the moving the zeroes to the end.: " << endl;
 for(int i = 0; i < n; i++) cout << arr[i]  << " ";
 cout << endl;
}

vector<int> optimal(vector<int>& arr, int n){
  int j = -1;
  //FIXME: here we are using two pointer method. 
  for(int i = 0 ; i < n ; i++){
    if(arr[i] == 0){
      j = i;
      break;
    }
  }
  //TODO: initialising j to -1, and then finding the element which is zero, update the j value with the zero element index.
  if(j == -1) return arr; //TODO: if still j value is -1, that means we don't have a zero in our array.
  for(int i = j + 1; i < n; i++){
    if(arr[i] != 0){
      swap(arr[i], arr[j]);
      j++;
    }
  }
  //TODO: in the above code , we start from j + 1, if we find a non-zero element we swap that with the jth array element, and then 
  // and then we increment j value. 
  return arr;
}
int main(){
  vector<int> arr{2,0,2,0,3,4,5,65,0,2,0};
  int n  = arr.size();
  cout << "Before removing the zeroes : " << endl;
  for(int i = 0 ; i < n; i++) cout << arr[i] << " ";
  cout << endl;
  brute(arr,n);
  vector<int> ans = optimal(arr,n);
  for(int i = 0; i < n; i++) cout << ans[i] << " ";
  cout << endl;
  return 0;
}
