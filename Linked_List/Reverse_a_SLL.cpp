//FIXME: We have to reverse a singly Linked List.
#include<bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int val) : data(val), next(nullptr) {}
};

//TODO: this is the function to reverse a singly linked list.
Node* reverseLinkedList(Node* head){
  Node* curr = head; //NOTE: this is used to traverse the linked list.
  Node* prev = nullptr; //NOTE: this represents the previous node.
  Node* next = nullptr; //NOTE: this represents the next node of the linked list.

  while(curr){
    next = curr->next; //NOTE: first we store the next node to next pointer, because we only have next pointer in the SLL.
    curr->next = prev; //NOTE: so how do we store previous when we don't have curr->prev, simple, we start prev from nullptr.
    prev = curr; //NOTE: And then as move to the next node, we point the prev to the current node.
    curr = next; //NOTE: This is moving on to the next node.
  }
  return prev; //NOTE: at the end, returning prev because curr will be pointing to nullptr and prev is obv one step behind.(always) 
}

void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);

    cout << "Original List: ";
    printList(head);

    head = reverseLinkedList(head);

    cout << "Reversed List: ";
    printList(head);

    return 0;
}
