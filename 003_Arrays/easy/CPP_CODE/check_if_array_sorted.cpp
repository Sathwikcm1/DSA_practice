//FIXME: so the question is the we have to check if the array is sorted or not.
#include<bits/stdc++.h>
using namespace std;

bool brute_force(vector<int> arr, int n){ // it starts from 1 because the first one will make ar[i-1] go out of bound.
  for(int i = 1 ; i < n ; i++){
    if (arr[i] < arr[i -1 ]){ // if current element is smaller than the previous element then we return false indicating that array isn't sorted.
      return false;
    } 
  }
  return true; //otherwise we return true.
}
// this is the optimal solution, the brute force would use nested for loops to find out this thing.
int main(){
  vector<int> arr{2,5,6,7,8,9,10};
  int n = arr.size();
  cout << "Brute force approach: " <<   (brute_force(arr,n) == 1 ? "The array is sorted" : "No the array is not sorted") << endl;

  return 0;
}
