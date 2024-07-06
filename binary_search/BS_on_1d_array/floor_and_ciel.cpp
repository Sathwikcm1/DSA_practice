#include<bits/stdc++.h>
using namespace std;
                                                                            //! page no : 90.
int findFloor(int arr[], int n, int x) {
	int low = 0, high = n - 1;
	int ans = -1;

	while (low <= high) {
		int mid = (low + high) / 2;
		// maybe an answer
		if (arr[mid] <= x) {
			ans = arr[mid];
			//look for smaller index on the left
			low = mid + 1;
		}
		else {
			high = mid - 1; // look on the right
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
	int arr[] = {3, 4, 4, 7, 8, 10};
	int n = 6, x = 5;
	pair<int, int> ans = getFloorAndCeil(arr, n, x);
	cout << "The floor and ceil are: " << ans.first << " and " << ans.second << endl;
	return 0;
}