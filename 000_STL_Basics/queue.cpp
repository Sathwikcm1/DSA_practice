#include <bits/stdc++.h>

using namespace std;
                             //? A queue is a container which stores elements in a first in first out manner. so you can keep on pushing , when you pop the last element will be removed.
int main() {
    queue<int> q;               // Declare a queue of integers

    q.push(10);                 // Insert element at the back
    q.push(20);
    q.pop();                    // Remove element from the front
    q.push(30);
    int front = q.front();      // Access the front element
    int back = q.back();        // Access the back element
    bool isEmpty = q.empty();   // Check if queue is empty
    int size = q.size();        // Get number of elements
    cout << front << " " << back << " " << isEmpty << " " << size << endl;

    return 0;
}
