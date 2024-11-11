// finding gcd of hcf of two numbers
#include<bits/stdc++.h>                         //!page no : 3
using namespace std;

#define ll long long

int brute_force(int n, int m){  // brute approach time complexity : O(min(n,m))
int gcd = 1;
    for(int i = 1; i <= min(n,m); i++){     // we are looping from 1 to min(n,m) and checking if i is a factor of both n and m, we select the smallest number as i.
        if(n%i == 0 && m%i == 0){
        gcd = i;
    }
}
return gcd;             // and return the gcd
}

int better_approach(int n , int m){             // time complexity : O(min(n,m)) still the same , but somewhat better because we start from the back.
    for(int i = min(n,m); i > 0; i--){
        if(n%i == 0 && m%i == 0) return i;
    }
    return 1;   // because the hcf of 0 and any number is 0. and hcf of 1 and any number is 1.
}

int optimal_approach(int n , int m){            // time complexity : O(min(n,m)) and space complexity : O(1) for every algorithm here.
    while(n > 0 && m > 0){
        if(n > m) n %= m;
        else m %= n;
    }
    if(n == 0) return m;
    else return n;
}



int main() {
    int n = 5;
    int m = 10;
    cout << "This is the brute force approach : " << brute_force(n,m) << endl;
    cout << "This is the better approach : " << better_approach(n,m) << endl;
    cout << "This is the optimal approach: " << optimal_approach(n,m) << endl;
    return 0;
}

//vector<long long> lcmAndGcd(long long A , long long B) {          // this one's got more lcm and also got gcd.
        // code here
//         long long originalA = A, originalB = B;

    // Compute GCD using the Euclidean algorithm
//     while (B != 0) {
//         long long temp = B;
//         B = A % B;
//         A = temp;
//     }
//     long long gcd = A;

    // Compute LCM using the relation LCM * GCD = A * B
//     long long lcm = (originalA / gcd) * originalB;

    // Return the results as a vector
//     return {lcm, gcd};
//     }
