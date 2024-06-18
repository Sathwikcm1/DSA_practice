#include <stack>
using namespace std;

int main() {
    stack<int> s;               // Declare a stack of integers

    s.push(10);                 // Insert element at the top
    s.push(20);
    s.pop();                    // Remove element from the top
    int top = s.top();          // Access the top element
    bool isEmpty = s.empty();   // Check if stack is empty
    int size = s.size();        // Get number of elements

    return 0;
}
