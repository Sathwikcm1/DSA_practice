//FIXME : Rotate the array by given k places. just like previous question but more for particular k places.
#include<bits/stdc++.h>
using namespace std;
void brute(vector<int>& arr,int k, int n){
  //TODO: so first, we take the kth and next places and put it in a temp array. 
  //todo and then we can start from n - k - 1, remaining places from the last, we keep on shifting .
  //then at the end we copy the from temp array to the original to fill the beginning of the array.
 if(n == 0)
   return;
 k = k % n; // this is here because if the k value is greater than the size of the array, then the remainder will do just fine in that case.
 if ( k > n)
   return;
 vector<int> temp(k);
 for(int i = n - k; i < n; i++){ //NOTE: this is where we are copying end elements to the temp array.
   temp[i - n+ k] = arr[i];
 }
 for(int i = n - k - 1; i >= 0; i--){ //NOTE: this is where we shifting elements to the back, making space in the front for the new elements.
   arr[i + k] = arr[i];
 }
 for(int i = 0 ; i < k ; i++){ //NOTE: this is where we are doing copying from the temporaray array to the original array.
   arr[i] = temp[i];
 }
}
int main(){
  vector<int> arr{1,2,3,4,5,6,7};
  int n = arr.size();
  int k = 2; //TODO: no places that has to be rotated.
  brute(arr,k,n);
  cout << "After rotation of the array: " << endl;
  for(int i = 0 ; i < n ;i++) cout << arr[i] << " ";
  cout << endl;
  return 0;
}
