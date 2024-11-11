#include<bits/stdc++.h>
using namespace std;
#define ll long long

// this problem is basically that they will provide a number , we just have to tell if it is palindrome or not 
//! page no : 2
string optimal(int n){
	ll rev_no = 0;
	ll og = n;
	while(n > 0){
		int ld = n%10;
		rev_no = (rev_no * 10) + ld;
		n = n/10;
	}
	if(rev_no == og) return "True";
	else
	return "False";
}

int main(){
	int n = 4554;
	cout << optimal(n)<< endl;
	return 0;
}
