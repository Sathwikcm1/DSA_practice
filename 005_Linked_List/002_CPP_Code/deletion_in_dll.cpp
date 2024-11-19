#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
  //TODO: yhes you don't need to write public shit tonna times, it is enough if we write it once at the start.
    int data;
    Node* next;
    Node* back;

    // Constructor for creating a node with data and pointers //TODO: cool constructor by chatgpt, it has default values.
    // TODO: if the values are not provided by the user we can always depend on the default value which is nullptr.
    Node(int data1, Node* next1 = nullptr, Node* back1 = nullptr) {
        data = data1;
        next = next1;
        back = back1;
    }
};

// Function to convert an array into a doubly linked list
// TODO: this is used to convert an array into a DLL.
//
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
// TODO: this function is to delete the head of the LInked list.
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
// TODO: function to delete the tail of the DLL.
// so cases are that if no node present in the dll.
// and the next is only one node is present.
// and the rest a whole linked list is present.
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
    //NOTE: this goes till the last node and stops so currently temp is pointing to the last node which we are suppose to delete.
    // Now temp is pointing to the last node
    // create a new node for the previous node.
    Node* prevNode = temp->back; // Get the second last node

    // Update pointers
    // NOTE: so we update the pointers saying that previous node's next is poiting to nullptr. 
    prevNode->next = nullptr; // Remove reference to last node
                              // NOTE: and the rest is just to delete current node that is temp.
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

//NOTE: This is about deleting a node in kth position.
// how do we do this, again cases. so the cases are if no nodes is present we simply just return nullptr.
// if not, if the nodes are present. we have a cnt that counts the index of nodes it is currently pointing to.
Node* remove_kth_node(Node* head,int k){
  Node* curr = head;
  if(head == nullptr) return nullptr;

  int cnt = 0;
  while(curr){
    cnt++;
    if(cnt == k) break; //NOTE: if we find the k position, then we break out of the loop.
    curr = curr->next;
  }
  //TODO: once we reach the kth node. we will have two new nodes the previous one and the next one.
  Node* prev_Node = curr->back;
  Node* next_Node = curr->next;
  
  if(prev_Node == nullptr && next_Node == nullptr) return nullptr; //TODO: this means only one node exists in the linked list and that is current node.and so we politely return nullptr.
  
  else if(prev_Node == nullptr) //TODO: this means the given node is the head.
    return delete_head(head);
  else if(next_Node == nullptr) //TODO: this means the given node is the tail.
    return delete_tail(head);
  prev_Node->next = next_Node; //TODO: otherwise if there is any middle ones. we change the previous node's next to next_Node and vice versa.
  next_Node->back = prev_Node;
  curr->next = nullptr;
  curr->back = nullptr;
  delete curr;
  return head;
}


//NOTE: we will be given a node which we have to remove based on the value.
//in this one we are given just the node itself no head will be given, and the value of k is never head
void delete_given_node(Node* curr){
  Node* prev_Node = curr->back;
  Node* next_Node = curr->next;
  //TODO: what if the next_Node is pointing to nullptr which means the current node is the last node.
  if(next_Node == nullptr){
    prev_Node->next = nullptr;
    curr->back = nullptr;
    delete curr;
    return;
  }
  //TODO: what if the it has both next_Node and the prev_Node.
  prev_Node->next = next_Node;
  next_Node->back = prev_Node;
  curr->next = nullptr;
  curr->back = nullptr;
  delete curr;
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
  Node* temp = remove_kth_node(head,3);
  cout << "After removing the 3rd node in the current linked list." << endl;
  while(temp){
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
  delete_given_node(head->next);
  temp = head;
  cout << "After removing the node right after the head." << endl;
  while(temp){
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
	return 0;
}
