// basically we will be given a list of intervals and we have to merge all the overlapping intervals and return it.

#include<bits/stdc++.h>
using namespace std;

#define ll long long

vector<vector<int>> brute_force(vector<vector<int>> arr){
    int n = arr.size();
    sort(arr.begin(),arr.end());                //? first we sort the array so comparing would become in O(nlogn).
    vector<vector<int>> ans;                    //? ans vector to store the merged intervals.
    for(int i = 0; i<n;i++){                    //? here we iterate through the array.
        int start = arr[i][0];                  //? start and end are the starting and ending points of the intervals.
        int end = arr[i][1];

        if (!ans.empty() && end <= ans.back()[1]) {     //? if the answer is not empty and the end point of the current interval is less than or equal to the end point of the last interval we merge the intervals.
            continue;                                   //? we wouldn't do anything because the intervals are already merged.
        }

        for(int j = i+1;j<n;j++){                       //? now we iterate through the remaining intervals. so we start from the next interval.
            if (arr[j][0] <= end) {                     //? if the start point of the current interval is less than or equal to the end point of the last interval we merge the intervals.
                end = max(end, arr[j][1]);              //? we update the end point of the last interval.
            }
            else {
                break;                                  //? if the start point of the current interval is greater than the end point of the last interval we break the loop.
            }
        }
        ans.push_back({start, end});                    //? we push the merged intervals in the ans vector.
    }
    return ans;
}

int main() {
    vector<vector<int>> arr = {{1, 3}, {8, 10}, {2, 6}, {15, 18}};
    vector<vector<int>> ans = brute_force(arr);
    cout << "The merged intervals are: " << "\n";
    for (auto it : ans) {
        cout << "[" << it[0] << ", " << it[1] << "] ";
    }
    cout << endl;
    return 0;
}