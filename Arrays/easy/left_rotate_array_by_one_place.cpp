//FIXME: we have to rotate the array by 1 time. the first elmenet should be at last position.
#include<bits/stdc++.h>
using namespace std;

void brute(vector<int>& arr, int n ){ //we are basically making a temporary array , and putting all the elements into it from first index, at last we put the arr[0].
  vector<int> temp(n);
  for(int i = 1; i < n ; i++){ //TODO: well notice that it starts from 1 here. because the first element is put later.
    temp[i - 1] = arr[i];
  } 
  temp[n - 1] = arr[0]; //NOTE: this where we insert the first element at the last position.
  for(int i = 0 ; i < n; i++){
    cout << temp[i] << " "; // rearranging the original array using the temporary array.
  }
  cout << endl;
}
void optimal(vector<int>& arr, int n){ // same shit different way of writing.
  int temp = arr[0];
  for(int i = 0 ; i < n - 1; i++){
    arr[i] = arr[i + 1];
  }
  arr[n - 1] = temp;
  for(int i = 0 ;i < n; i++){
    cout << arr[i] << " ";
  }
  cout << endl;
}
int main(){
  vector<int> arr{1,2,3,4,5,6};
  int n = arr.size();
  cout << "Before doing the rotation: " << endl;
  for(int i = 0 ; i < n ;i++){
    cout << arr[i] << " ";
  }
  cout << endl;
  cout << "After the rotation of the array: " << endl;
  brute(arr,n);
  cout << endl;
  cout << "Optimal : does it one for loop " << endl;
  optimal(arr,n);

  return 0;
}
