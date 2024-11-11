//! The question we are suppose to find the ceil and floor of the given x or target, for example in arr[] = {10,20,25,30,40} for x = 27, ceil = 30 and floor = 25.
//! and for 25 in the same ceil = 25 and floor = 25. if x is present in the array then the floor = x and ceil = x.

#include<bits/stdc++.h>
using namespace std;
                                                                            //! page no : 90.
int findFloor(int arr[], int n, int x) {			//? finding the floor and ceil using binary search.
	int low = 0, high = n - 1;						//? we usually start from the low index and end at the high index.
	int ans = -1;									//? answer is initialised to -1 because if the target is not present in the array then we return -1.

	while (low <= high) {
		int mid = (low + high) / 2;
		// maybe an answer
		if (arr[mid] <= x) {						//? if the middle element is less than x, firstly we add the mid element to the ans and then we increase the low to mid + 1;
			ans = arr[mid];
			//look for smaller index on the left    //?  because the if the mid element is less than it might be an answer , but also there might exist an element that is grater than the current element but also just less than x.
			low = mid + 1;
		}
		else {
			high = mid - 1; // look on the right	//? if the mid element is greater than x. then we decrease the high = mid - 1. because we find another element that is less than or equal to x.
		}
	}
	return ans;
}

int findCeil(int arr[], int n, int x) {             //? this is basically finding the lower bound.
	int low = 0, high = n - 1;				
	int ans = -1;

	while (low <= high) {
		int mid = (low + high) / 2;
		// maybe an answer
		if (arr[mid] >= x) {                        //? if the mid index is greater than the target or not if it is then we decrease the high pointer so that we can get the next index.
			ans = arr[mid];
			//look for smaller index on the left
			high = mid - 1;                         //? else we increase the low pointer so that we can get the next index.
		}
		else {
			low = mid + 1; // look on the right
		}
	}
	return ans;                                               //? otherwise we return the ans.  
}

pair<int, int> getFloorAndCeil(int arr[], int n, int x) {  //? this function is basically used to generate the pair.
	int f = findFloor(arr, n, x);
	int c = findCeil(arr, n, x);
	return make_pair(f, c);             //? make pair is used to generate the pair.
}

int main() {
	int arr[] = {3, 4, 4,5, 7, 8, 10};
	int n = 6, x = 5;
	pair<int, int> ans = getFloorAndCeil(arr, n, x);
	cout << "The floor and ceil are: " << ans.first << " and " << ans.second << endl;
	return 0;
}