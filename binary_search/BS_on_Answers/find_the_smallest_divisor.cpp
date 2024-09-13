//! the question is find the smallest divisor such that the sum of all the elements in the array is greater than the given threshold.
//! example : Explanation for Sample Input 1 :
//! We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
//! The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor, and the sum is 7(1 + 1 + 1 + 2 + 2) if we choose 3 as a divisor, which is less than the 'limit'.
//! Hence we return 3.
//? it is like this arr{1,2,5,9} and threshold = 7, so divisor = 5 , 1/5 ceil value = 1, 2/5 ceil value is 1, 5/5 ceil value is 1, 9/5 ceil value is 2, so the total sum is 1+1+1+2 = 4. which is less than 7 , so divisor = 5 is one of the answers but we need to find the smallest one.

#include<bits/stdc++.h>
using namespace std;
#define ll long long

int brute_force(vector<int> arr, int limit){            //? this is brute force approach that takes O(n * maxi).
    
    for(int d = 1; d < limit; d++){                     //? this is loop of divisors goes from 1 to threshold.
        int sum = 0;                                    //? this is sum of all the elements in the array.
        for(int i = 0; i < arr.size(); i++){            //? this is loop goes through the array.
            sum += ceil((double) arr[i] / (double) d);  //? adding the sum of all  the  ceil elements when divided by the divisor.
        }
        if(sum <= limit) return d;                      //? if the sum is less or equal to the threshold then we return the divisor.
    }
    return -1;                                          //? otherwise we return the -1.
}

int sumofdivisors(int divisor, vector<int> arr){
    int sum = 0;
    for(int i = 0 ; i < arr.size(); i++){
        sum += ceil((double) arr[i]/ (double) divisor);
    }
    return sum;
}
int optimal_approach(vector<int> arr, int threshold){
    int low = 1, high = *max_element(arr.begin(),arr.end()); //todo finding out the low and high values in the array.
    while(low<= high){
        int mid = (low+high)/2;
        if(sumofdivisors(mid, arr) <= threshold){
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }
    return low;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int limit = 8;
    int ans = brute_force(arr, limit);
    cout << "The minimum divisor is: " << ans << "\n";
    cout << "This is using optimal approach: \n";
    cout << optimal_approach(arr, limit);
    cout << endl;
    return 0;

}