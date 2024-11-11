#include<bits/stdc++.h>
using namespace std;
                                            //? A Collection of unique elements in a specific order.
#define ll long long                        // time complexity for operations :  O(log n) for insertion,  deletion, searching and other operations.

int main() {
    set <int> s;
    set <int> v = {1, 2, 3, 4, 5}; // can also declare and initialize
    s.insert(1);                        // this is how to insert
    s.erase(s.begin());                     // this line erases the first element
    for(int i = 0; i< 10; i++) s.insert(i); // then we are adding the elements from 0 to 9.
    for(auto it : s) cout << it << " ";         // printing elements using iterators since we can't just print them using normal int.
    cout << "\n";
    for(auto it = s.begin(); it != s.end(); it++)       // printing elements using iterators , another way.
{
    cout << *it << " ";
}    cout << s.size() << endl;               // this line gives the size of the set.

    if(s.find(2) != s.end()) cout << "The set contain 2." << endl; // this checks if 2 is present in the set or not.

    s.clear(); // again this would clear the set completely.
    if(s.empty()) cout << "The set is empty"<< endl;
    return 0; 
}