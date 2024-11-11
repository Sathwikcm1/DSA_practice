// basically we are printing the name n times using recursion.

#include<bits/stdc++.h>
using namespace std;

#define ll long long

void func(string name,int n){                       // time complexity : O(n) and space complexity : O(n). we are just printing the names n times.
    if(n == 0) return;                              // base case. if this is not present then it will go in infinite loop.
    cout << name << endl;
    func(name,n-1);
}

int main() {
    string name; cout << "Enter the name: ";
    cin >> name;
    int n;  cout << "\n Enter the number of time it should be repeated."<<endl;
    cin >> n;
    func(name , n);
    return 0;
}