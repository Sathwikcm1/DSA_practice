#include<bits/stdc++.h>
using namespace std;
//TODO: just a normal linear search in the array. not a big deal.

int main(){
  int arr[] = {1,2,3,4,5,6};
  int n = sizeof(arr)/sizeof(arr[0]);
  int k = 3;

  for(int i = 0 ; i < n ;i++) {
    if(arr[i] == k) cout << "The element is present." << endl;
  }
  return 0;
}
