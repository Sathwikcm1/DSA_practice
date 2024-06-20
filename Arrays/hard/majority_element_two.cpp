// basically the same as n/2 times majority problem, we will return the a list of elements that occurs more than n/3 times. n being the size of the array.
#include<bits/stdc++.h>
using namespace std;

#define ll long long

vector<int> brute_force(vector<int> arr, int n) {       // this is the brute force approach, time complexity : O(n^2) and space complexity : O(1).
    vector<int> ans;
    for(int i = 0; i < n; i++){                     // iterating throgh the array.
        if(ans.size() == 0 || ans[0] != arr[i]){        // the size of the ans, will be 2. because of only 2 elements that occurs more than n/3 times.
            int cnt = 0;
            for(int j = 0; j < n;j++){
                if(arr[j] == arr[i]) cnt++;            // counting the number of occurences of the element.
            }
            if(cnt > n/3) ans.push_back(arr[i]);        // if the count is more than n/3, then we push the element in the ans.
        }
        if(ans.size() == 2) break;                     // if the size of the ans is 2, then we break the loop.
    }
    return ans;                                        // return the ans.
}


vector<int> better_approach(vector<int> arr, int n){        // this is the better approach, time complexity : O(n) and space complexity : O(n).
    vector<int> ans; int mini = (n/3)+1;            // we are basically doing a hashmap to store the frequency of the elements. and then we find the minimum frequency. if the frequency is more than n/3, then we push the element in the ans.
    unordered_map<int,int> mp;
    for(int i = 0; i < n; i++){
        mp[arr[i]]++;
        if(mp[arr[i]] == mini) ans.push_back(arr[i]);
        if(ans.size() == 2) break;                  // if the size of the ans is 2, then we break the loop. because that is the ans.
    }
    return ans;
}
int main() {
    vector<int> arr{1,2,2,2,2,3,3,3,3};
    int n= arr.size();
    vector<int> ans = brute_force(arr,n);
    for(auto it : ans) cout << it << " " << endl;
    cout << "This is using better approach: \n";
    vector<int> an = better_approach(arr,n);
    for(auto it: an) cout<< it << " " << endl;
    return 0;
}