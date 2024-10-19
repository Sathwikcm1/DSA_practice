#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* back;

    // Constructor for creating a node with data and pointers
    Node(int data1, Node* next1 = nullptr, Node* back1 = nullptr) {
        data = data1;
        next = next1;
        back = back1;
    }
};

// Function to convert an array into a doubly linked list
Node* convert_arr_DLL(const vector<int>& arr) {
    if (arr.empty()) return nullptr; // Handle empty array case

    Node* head = new Node(arr[0]);
    Node* prev = head;

    for (size_t i = 1; i < arr.size(); i++) {
        Node* temp = new Node(arr[i], nullptr, prev);
        prev->next = temp;
        prev = temp;
    }
    
    return head;
}

// Function to delete the head of the doubly linked list
Node* delete_head(Node* head) {
    if (head == nullptr) return nullptr; // List is empty

    Node* newHead = head->next; // Move head to next node
    if (newHead != nullptr) {
        newHead->back = nullptr; // Update back pointer of new head
    }
    
    delete head; // Delete old head
    return newHead; // Return new head
}

// Function to delete the tail of the doubly linked list
Node* delete_tail(Node* head) {
    if (head == nullptr) return nullptr; // List is empty

    if (head->next == nullptr) { // Only one node exists
        delete head; // Delete it
        return nullptr; // Now list is empty
    }

    Node* temp = head;

    // Traverse to find the last node
    while (temp->next != nullptr) {
        temp = temp->next;
    }

    // Now temp is pointing to the last node
    Node* prevNode = temp->back; // Get the second last node

    // Update pointers
    prevNode->next = nullptr; // Remove reference to last node
    delete temp; // Delete last node
    
    return head; // Return original head
}

// Function to print the list from head to tail
void print_list(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    vector<int> arr{1, 2, 3, 4, 5, 6};
    
    Node* head = convert_arr_DLL(arr);
    
    cout << "Original List: ";
    print_list(head);

    cout << "After deleting the head of the Linked List:" << endl;
    head = delete_head(head);
    print_list(head);

    cout << "After deleting the tail of the Linked List:" << endl;
    
	// Important: Update head after deleting tail
	head = delete_tail(head);
	print_list(head);

	return 0;
}
