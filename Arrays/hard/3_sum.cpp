// basically the two sum problem only  but we have to return that list of triplets that sum up to zero.
#include<bits/stdc++.h>
using namespace std;                                //! page no : 75.

#define ll long long

vector<vector<int>> brute_approach(vector<int> arr, int n){         // this takes the time complexity to O(n^3) * O(logn). and space complexity to O(1).
    set<vector<int>> st;                // this is the set to store the triplets that sum up to zero.
    for(int i = 0; i < n; i++){         
        for(int j = i+1; j<n;j++){          
            for(int k =j+1; k<n;k++){           
                if(arr[i] + arr[j]+arr[k] == 0){            // we check if the sum of the triplets is zero. if it is we add that to a temp vector, sort it and then add it to the set. 
                                                                // we do this because we avoid the duplicate triplets in the set.
                    vector<int> temp{arr[i],arr[j],arr[k]};
                    sort(temp.begin(),temp.end());
                    st.insert(temp);
                }
            }
        }
    } 
    vector<vector<int>> ans(st.begin(),st.end());               // copying the elements from the set to the ans vector.
    return ans;                                         // and then we return the ans vector.
}

vector<vector<int>> better_approach(vector<int> arr, int n){        //todo time complexity : O(N2 * log(no. of unique triplets) and space complexity :  O(2 * no. of the unique triplets) + O(N).
    set<vector<int>> st;
    for(int i = 0; i< n;i++){                                   
        set<int> hashset;
        for(int j = i+1;j<n;j++){                           //todo this is basically hashing the array in the set., so we find the third element by the sum of two elements.
            int third = -(arr[i] + arr[j]);
            if(hashset.find(third) != hashset.end()){       //todo and check if the third element is present in the set or not. if it is present then we add the triplets to the set.
                vector<int> temp {arr[i],arr[j],third};
                sort(temp.begin(),temp.end());              //todo first we sort the triplets., and then we add it to the set.
                st.insert(temp);                            //todo insert this triplet in the set.
            }
            hashset.insert(arr[j]);                         //todo insert the j element anyway in the set.
        }
    }
    vector<vector<int>> ans(st.begin(),st.end());           //todo copying the elements from the set to the ans vector.
    return ans;                                             //todo return the ans vector.
}

vector<vector<int>> optimal_approach(vector<int> arr, int n){  //? time complexity : O(NlogN)+O(N2) and space complexity : O(no. of quadruplets). 
    vector<vector<int>> ans;
    sort(arr.begin(),arr.end());                    //? so we first sort the array given to us we are using 2 pointers method here.
    for(int i = 0; i < n; i++){
        if( i != 0 && arr[i] == arr[i-1]) continue;      //? so we avoid the duplicate triplets. skips the remaining code if we find the duplicate triplet.
        int j = i+1;                                   //? so this is the second pointer.
        int k = n-1;                                    //? so this is the third pointer.
        while(j<k){                                     //? this should run till j crosses k.
            int sum = arr[i]+arr[j]+arr[k];             //? so we calculate the sum of the triplets.
            if(sum < 0) j++;                            //? if the sum is less than 0 then we increase the j pointer so that sum will be greater than 0.
            else if(sum > 0) k--;                       //? or else if the sum is greater than 0 then we decrease the k pointer so that sum will be less than 0 basically closer to zero.
            else{
                vector<int> temp = {arr[i],arr[j],arr[k]}; //? so we store the triplets in the temp vector.
                ans.push_back(temp);                                    //? and then we push it in the ans vector.
                j++; k--;                                           //? and then we increase and decrease the j and k pointers so that we can get the next triplets.
                while(j < k && arr[j] == arr[j-1]) j++;             //? and then we avoid the duplicate triplets.
                while(j < k && arr[k] == arr[k+1]) k--;
            }
        }
    }
    return ans;                                                     //? and then we return the ans vector.
}
int main() {
    vector<int> arr{-1,0,1,2,-1,-4};
    int n = arr.size();

    vector<vector<int>> ans = brute_approach(arr,n);
    for(auto it : ans){
        for(auto i : it) cout << i << " ";
        cout << endl;
    }
    cout << "This is using better approach: \n";
    vector<vector<int>> an = better_approach(arr,n);
    for(auto it : an){
        for(auto i : it) cout << i << " ";
        cout << endl;
    }
    cout << "This is using optimal approach: \n";
    vector<vector<int>> ani = optimal_approach(arr,n);
    for(auto it : ani){
        for(auto i : it) cout << i << " ";
        cout << endl;
    }
    return 0;
}