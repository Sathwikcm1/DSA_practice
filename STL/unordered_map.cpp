// An unordered_map in C++ STL is an associative container that stores elements in key-value pairs, where each key is unique and associated with exactly one value, and the elements are stored in an unordered manner
#include<bits/stdc++.h>
using namespace std;

#define ll long long        //? time complexity : best case : O(1), worst case : O(n). so be careful when using this.

int main() {
    unordered_map <int, int> m;
    unordered_map <int, string> s;
    unordered_map <int, int> v = {{1,1},{2,2},{3,3}};
    v[2]++;                                             // can increment the second element of the map using the key. this is useful in hasing problems.

    for(int i = 0; i < 10; i++){
        m[i] = i;
    }
    for(auto it = m.begin(); it != m.end(); ++it) {
        cout << it->first << " " << it->second << endl;
    }

    // Using range-based for loop
    for(const auto& p : m) {
        cout << p.first << " " << p.second << endl;
    }
    m.find(2); // find the element with key 2
    cout << "\n";
    cout << m.size() << endl; // gives the size of the map.
    m.clear(); // this would clear the whole map.
    return 0;
}   
