#include <bits/stdc++.h>
using namespace std;

#define ll long long

vector<vector<int>> brute_force(vector<int> arr, int n) { // this is basically the same thing we did for 2 sum and 3 sum
    set<vector<int>> st;

    // Iterate through each quadruplet combination
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) { // time complexity: O(n^4) and space complexity: O(n)
            for (int k = j + 1; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    long long sum = arr[i] + arr[j] + arr[k] + arr[l];
                    if (sum == 0) {
                        vector<int> temp = {arr[i], arr[j], arr[k], arr[l]};
                        // Sort the quadruplet to handle duplicates
                        sort(temp.begin(), temp.end());
                        // Insert the sorted quadruplet into the set
                        st.insert(temp);
                    }
                }
            }
        }
    }

    // Convert the set to a vector
    vector<vector<int>> ans(st.begin(), st.end());
    return ans;
}

vector<vector<int>> better_approach(vector<int> arr, int target, int n) { // time complexity: O(n^3) and space complexity: O(n)
    set<vector<int>> st;

    for (int i = 0; i < n; i++) { // this is basically hashing the array in the set, so we find the fourth element by the sum of three elements
        for (int j = i + 1; j < n; j++) {
            unordered_set<long long> hashset;
            for (int k = j + 1; k < n; k++) {
                long long sum = arr[i] + arr[j] + arr[k]; // so we find the fourth element by the sum of three elements
                long long fourth = target - sum;
                if (hashset.find(fourth) != hashset.end()) { // and check if the fourth element is present in the set or not. If it is present, then we add the quadruplets to the set
                    vector<int> temp{arr[i], arr[j], arr[k], int(fourth)};
                    sort(temp.begin(), temp.end());
                    st.insert(temp);
                }
                hashset.insert(arr[k]); // insert the k element anyway in the set. This is used for comparing the elements in the set
            }
        }
    }
    vector<vector<int>> ans(st.begin(), st.end());
    return ans;
}

vector<vector<int>> optimal_approach(vector<int> arr, int target, int n) {      //? we are basically using two pointers here., first i and j are for loop variables and then j and k are teh two pointers.
    sort(arr.begin(), arr.end());                                   // ? we first sort the array.
    vector<vector<int>> ans;

    for (int i = 0; i < n; i++) {
        if (i > 0 && arr[i] == arr[i - 1]) continue; // Avoid duplicates
        for (int j = i + 1; j < n; j++) {
            if (j != i + 1 && arr[j] == arr[j - 1]) continue; // Avoid duplicates
            int k = j + 1;                                      //? this is the pointer no 1, which is pointing to the third element.
            int l = n - 1;                                      //? this is the pointer no 2, which is pointing to the last element.
            while (k < l) {                                         //? this should run till k crosses l.
                long long sum = arr[i] + arr[j] + arr[k] + arr[l];      //? so we calculate the sum of the quadruplets.
                if (sum == target) {                                    //? if the sum is equal to target then we push the quadruplets in the ans vector.
                    vector<int> temp{arr[i], arr[j], arr[k], arr[l]};
                    ans.push_back(temp);
                    k++;
                    l--;
                    while (k < l && arr[k] == arr[k - 1]) k++; // Avoid duplicates  //? and then we increase and decrease the k and l pointers so that we can get the next quadruplets.
                    while (k < l && arr[l] == arr[l + 1]) l--; // Avoid duplicates
                } else if (sum < target) {                          //? or else if the sum is less than target then we increase the k pointer so that sum will be greater than target.
                    k++;
                } else {
                    l--;                                          //? or else if the sum is greater than target then we decrease the l pointer so that sum will be less than target basically closer to zero.   
                }
            }
        }
    }

    return ans;
}

int main() {
    vector<int> arr{1, 0, -1, 0, -2, 2};
    int n = arr.size();
    int target = 0;

    cout << "This is using brute force approach: \n";
    vector<vector<int>> ans = brute_force(arr, n);
    for (auto it : ans) {
        for (auto i : it) {
            cout << i << " ";
        }
        cout << endl;
    }

    cout << "This is using better approach: \n";
    vector<vector<int>> an = better_approach(arr, target, n);
    for (auto it : an) {
        for (auto i : it) {
            cout << i << " ";
        }
        cout << endl;
    }

    cout << "This is using optimal approach: \n";
    vector<vector<int>> ani = optimal_approach(arr, target, n);
    for (auto it : ani) {
        for (auto i : it) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}
