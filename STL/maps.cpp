//? map is a container that stores elements in sorted order with keys and values.
#include<bits/stdc++.h>
using namespace std;            // time complexity for the operations is O(log(n)).

#define ll long long

int main() {
    map <int,string> m;
    m[1] = "one";     // this is how we insert things in the map.
    map<int,string> mp = {{1,"one"},{2,"two"},{3,"three"}}; // we can do this one too.
    map<int,int> v = {{1,1},{2,2},{3,3}}; // we can also do this one too.
    v[2]++;                                 // if both are int we can just increase the value of the element like this.
    for(int i = 0; i < 10; i++){
        v[i] = i;
    }
    for(auto it : v) cout << it.first << "->" << it.second << endl;
    cout << endl;
    cout << "extra mod" << endl;
    map <int,int> mew;
    vector<int> some {1,2,3,4,5,5,2};
    for(int  ele : some){
        mew[ele]++;
    }
    for(auto it: mew) cout << it.first <<" ->" << it.second << endl;
    for(auto it: mew){
        if(it.second > 1) cout << it.first << "->" << it.second << endl;
    }
    m.erase(1); // removing the element with key 1.
    m.clear(); // this would again erase everything in the map.
    return 0;
}