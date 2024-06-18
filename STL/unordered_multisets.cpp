#include<bits/stdc++.h> // this is agian , but this time we are using unordered_multiset, it is a container that stores elements in no particular order with keys and values.
using namespace std;

#define ll long long

int main() {
    unordered_multiset <int> um;
    unordered_multiset <int> ums = {1,2,3,4,4};         // declaring the unordered_multiset and intializing it.
    for(int i = 0; i < 10; i++){
        um.insert(i);
    }
    cout << "Elements in the unordered_multiset um: \n";
    for(auto it: um) cout << it << " ";
    cout << "\n";
    ums.erase(ums.begin()); // this line erases the first element.
    cout << "Count of 2: " << ums.count(2) << endl; 
    if (ums.find(2) != ums.end()) {
        cout << "2 found in the unordered_multiset" << endl;
    }
    ums.clear(); // this would clear the whole set.
    return 0;
}