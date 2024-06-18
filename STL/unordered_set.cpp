#include<bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
    unordered_set<int> s;       // this is how we declare an unordered_set.
    unordered_set<int> uset = {1, 2, 3, 4, 5}; // declaring an unordered_set and intializing it.
    s.insert(1);               // this is how to insert in unordered_set.
    s.erase(s.begin());         // this line erases the first element.
    for(int i = 0; i< 10; i++) s.insert(i); // then we are adding the elements from 0 to 9.
    for(auto it : s) cout << it << " "; // then we are printing the elements; because we cannot print them using normal int, like we do with vectors.
    cout << "\n Printing using iterators: \n";
    for(auto it = s.begin(); it != s.end(); it++) cout <<  *it << " "; // can also print using iterators.
    cout << "\n";
    if(s.find(3) != s.end()) cout << "3 is present in the set s." << endl; // this checks if 3 is present in the set or not.
    // this works like if three is present in the set, it will print "3 is present in the set s." other it will point to the end. so it is not equal to the end we can print it.

    if(s.count(3) == 1) cout << "3 is present in the set s." << endl; // this checks if 3 is present in the set or not.
    // or we could erase within range like this :
    s.erase(s.begin(), s.end());
    for(auto it : s) cout << it << " ";
    cout << "\n";
    cout << s.size() << endl; // this line gives the size of the set.
    s.clear(); // this would clear the whole set.
    if(s.empty()) cout << "The set s is empty.";
    else cout << "The set s is not empty.";
    cout << "\n";
    return 0;
}