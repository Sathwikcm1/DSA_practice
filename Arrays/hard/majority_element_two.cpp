// basically the same as n/2 times majority problem, we will return the a list of elements that occurs more than n/3 times. n being the size of the array.
#include<bits/stdc++.h>
using namespace std;
                                                                        //! page no : 73
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


vector<int> better_approach(vector<int> arr, int n){        // this is the better approach, time complexity : O(n)*O(logn)->map and space complexity : O(n).
    vector<int> ans; int mini = (n/3)+1;            // we are basically doing a hashmap to store the frequency of the elements. and then we find the minimum frequency. if the frequency is more than n/3, then we push the element in the ans.
    unordered_map<int,int> mp;
    for(int i = 0; i < n; i++){                
        mp[arr[i]]++;
        if(mp[arr[i]] == mini) ans.push_back(arr[i]);
        if(ans.size() == 2) break;                  // if the size of the ans is 2, then we break the loop. because that is the ans.
    }
    return ans;
}

vector<int> optimal_approach(vector<int> arr,int n){        // this is the optimal approach, time complexity : O(n) and space complexity : O(1).
    int cnt1 = 0, cnt2 = 0;
    int ele1 = INT_MIN;                                 // this is moore's voting algorithm that is present in the majority element n/2 times problem.
    int ele2 = INT_MIN;
    for(int i = 0; i < n; i++){
        if(cnt1 == 0){                                  // we are applying the same thing here.
            cnt1 = 1;
            ele1 = arr[i];                          // so basically there is one extra count in this problem , because the ans vector can have only 2 items we have 2 count. so if the cnt1 is zero. we initialse the count to 1, and el is initialised with the current element of the array.
        }
        else if(cnt2 == 0){                         // the same way if cnt2 is also zero, we do the same process.
            cnt2 = 1;
            ele2 = arr[i];
        }
        else if(arr[i] == ele1) cnt1++;             // then we check if the element is the same or not. if it is we increase the respective cnt by 1, we do it for both the cnt 
        else if(arr[i] == ele2) cnt2++;
        else{
            cnt1--;                                 // otherwise we decrease the count by one.
            cnt2--;
        }
    }
    vector<int> ls;
    cnt1 = 0, cnt2 = 0;                         // checking the answer. reinitializing the cnt to zero. 

    for(int i = 0; i<n;i++){
        if(arr[i] == ele1) cnt1++;
        if(arr[i] == ele2) cnt2++;      
    }
    
    int mini = int(n/3) + 1;
    if(cnt1 >= mini) ls.push_back(ele1);        // if the cnts are more than the mini 
    if(cnt2 >= mini) ls.push_back(ele2);

    return ls;
}

int main() {
    vector<int> arr{1,2,2,2,2,3,3,3,3};
    int n= arr.size();
    vector<int> ans = brute_force(arr,n);
    for(auto it : ans) cout << it << " " << endl;
    cout << "This is using better approach: \n";
    vector<int> an = better_approach(arr,n);
    for(auto it: an) cout<< it << " " << endl;
    cout << "This is using optimal approach: \n";
    vector<int> ani = optimal_approach(arr,n);
    for(auto it: ani) cout<< it << " " << endl;
    return 0;
}