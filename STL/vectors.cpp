#include<bits/stdc++.h>                                     // this is related to StL vectors.
using namespace std;

#define ll long long

int main() {
    vector<int> v;  //? declaring a vector.
    vector<int> s{1,2,3,4,5};       // ? initializing a vector. can also do it like this or s = {1,2,3,4,5}; like this.
    for(int i = 0 ; i< 5; i++) cout << s[i] << " ";     //? printing the vector. can also do it using an iterator.
    for(int i = 0; i < 10; i++) v.push_back(i);
    // we can also insert to a vector by using this ; 
    v.insert(v.begin(), 0); // inserting 0 at the beginning of the vector. or can insert at the end as well.
    v.insert(v.end(),69);
    cout << "\n";
    cout << v.back(); // this returns the last element of the vector. 
    cout << "\n";
    cout << v.front(); // this returns the first element of the vector.
    v.pop_back(); // deletes the last element of the vector.
    cout << "\n";
    cout << "These are all the elements present inside the vector v: \n";
    for(auto it: v) cout<< it << " ";                                       //? printing elements using an iterator.
    cout << "\n";
    cout << "The size of the vector is given by v.size() : " << v.size() << endl;   

 if (find(v.begin(),v.end(),3) != v.end()) {                            //? we cannot use find in vectors., instead we have to use an iterator.
        cout << "3 is present in the vector v." << endl;
    } else {
        cout << "3 is not present in the vector v." << endl;
    }  
    if(v.empty()) cout << "The vector v is empty." << endl; else cout << "The vector is not empty.\n";
    v.clear(); // this would clear the whole vector.
    return 0;
}