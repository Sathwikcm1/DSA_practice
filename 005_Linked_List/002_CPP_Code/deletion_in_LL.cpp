//FIXME: this program is about deletion in Linked list.
//deletion of head, tail, deleting in the middle , deleting in kth position, deleting the given value node.
#include <bits/stdc++.h>
using namespace std;
//TODO: this is as usual defining the class and the constructors for the node creation.
class Node {
public:
    int data;
    Node* next;

    Node(int data1, Node* next1) { //TODO: construcotr 1
        data = data1;
        next = next1;
    }

    Node(int data1) { //TODO: constructor 2
        data = data1;
        next = nullptr;
    }
};

//TODO:  Convert array into a linked list.
Node* append_nodes(vector<int> arr) {
    int n = arr.size();
    Node* head = new Node(arr[0]);
    Node* temp = head;
    for (int i = 1; i < n; i++) {
        Node* n = new Node(arr[i]);
        temp->next = n;
        temp = n;
    }
    return head;
}

//NOTE:  Delete the head of the linked list.
Node* delhead(Node* head) {
    if (head == nullptr) return nullptr; //TODO: condition if the linked list is already empty.
    Node* temp = head;
    head = head->next;
    delete temp;
    return head;
}
//NOTE: simple enough for deleting the head of the node, make a temp for head, and free the temp and move the head to head->next.




//NOTE: Delete the tail of the linked list.
Node* deltail(Node* head) {
    if (head == nullptr) return nullptr; //TODO: List is empty
    if (head->next == nullptr) { //TODO: Only one node in the list
        delete head;
        return nullptr;
    }

    Node* temp = head;
    while (temp->next->next != nullptr) {
        temp = temp->next; // Move to the second-to-last node
    }

    delete temp->next; //TODO:  Delete the last node, first we free the memory and then point the pointer to nullptr;
    temp->next = nullptr; // Set the second-to-last node's next to null
    return head; // Return the updated head
}

//NOTE: deleting kth position node. k will be given.
Node* delete_k(Node* head, int k){
  if(head == nullptr ) return nullptr;
  if ( k == 1){ //TODO: this is for if first node has to be deleted, we move the head to next node, and free the memory of the prev stored temp node.
    Node* temp = head;
    head = head->next;
    delete temp; //TODO: freeing the memory of the previous head.
    return head;
  }
  
  Node* prev = nullptr; //TODO: a pointer to point to the previous node to the current node.
  int cnt = 0; //TODO: a counter to count the nodes.
  Node* temp = head; //TODO: a pointer to point to the current node while traversing.
  while(temp){
    cnt++;
    if(cnt == k){ //TODO: if the count matches the k, then we set the previous of next to next of previous of next, skipping the one in the middle.
      prev->next = prev->next->next;
      delete temp;//TODO: before we move on we have to delete the memory of that skipped node. 
      break;
    }
    prev = temp; //TODO: this is for storing the previous node.
    temp = temp->next;
  }
  //NOTE: don't have to worry about writing a separate case for deleting the last node. the above code will handle that too.
  return head;
}

//TODO: deleting by the value of the node.
Node* remove_val(Node* head, int val){
  if(head == nullptr ) return nullptr;
  if(head->data == val) {
    Node* temp = head;
    head = head->next;
    delete temp;
    return head;
  }

    Node* temp = head;
    Node* prev = nullptr;

    while(temp){
      if(temp->data == val){
        prev -> next= prev->next->next;
        delete temp;
        break;
      }
      prev = temp;
      temp = temp->next;
    }
    return head;
}




int main() {
    vector<int> arr{1, 2, 3, 4, 5, 6};
    Node* head = append_nodes(arr);

    // Print the linked list
    cout << "Original list: ";
    Node* temp = head;
    while (temp) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;

    // Delete the head of the linked list
    head = delhead(head);
    cout << "After deleting the head: ";
    Node* temp2 = head;
    while (temp2) {
        cout << temp2->data << " ";
        temp2 = temp2->next;
    }
    cout << endl;

    // Delete the tail of the linked list
    head = deltail(head); // Update head after deleting the head
    cout << "After deleting the tail: ";
    Node* mew = head;
    while (mew) {
        cout << mew->data << " ";
        mew = mew->next;
    }
    cout << endl;
    cout << "After deleting a node at position 3. " << endl;
    head = delete_k(head,3);
    Node* woof = head;
    while(woof){
      cout << woof->data << " ";
      woof = woof->next;
    }
    cout << endl;
    
    cout << "Removing the node whose value is 3. " << endl;
    head = remove_val(head,3);
    Node* tempo = head;
    while(tempo){
      cout << tempo->data << " ";
      tempo = tempo->next;
    }
    cout << endl;
    return 0;
}
