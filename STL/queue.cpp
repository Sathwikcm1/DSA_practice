#include <queue>
using namespace std;

int main() {
    queue<int> q;               // Declare a queue of integers

    q.push(10);                 // Insert element at the back
    q.push(20);
    q.pop();                    // Remove element from the front
    int front = q.front();      // Access the front element
    int back = q.back();        // Access the back element
    bool isEmpty = q.empty();   // Check if queue is empty
    int size = q.size();        // Get number of elements

    return 0;
}
