// we are reversing an array using recursion

#include<bits/stdc++.h>                                                             //! page no : 27.
using namespace std;

#define ll long long

void reversee(int arr[],int i, int n){
    if(i >= n/2) return;                    // it should go till half of the array. because the other half is already reversed.
    swap(arr[i],arr[n-i-1]);
    reversee(arr,i+1,n);                    // time complexity : O(n) and space complexity : O(1)., just increase the i while calling the function again.
}
int main() {
    int arr[] = {1,2,3,4,5};
    reversee(arr,0,5);
    for(int i = 0; i < 5; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}