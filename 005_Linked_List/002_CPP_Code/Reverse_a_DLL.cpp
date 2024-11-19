#include<bits/stdc++.h>
using namespace std;

class Node{
  public:
    Node* prev;
    int data;
    Node* next;

    Node(Node* prev1 = nullptr, int data1 = 0, Node* next1 = nullptr){
       prev = prev1;
       data = data1;
       next = next1;
    }
};


//TODO: this function basicallay converts an array into a DLL.

Node* convertARR2DLL(vector<int> &arr) {
    Node* head = new Node(nullptr, arr[0], nullptr); // Create head node
    Node* prev = head;
    
    for(size_t i = 1; i < arr.size(); i++) {
        Node* curr = new Node(prev, arr[i], nullptr); // Create new node and link it
        prev->next = curr;
        prev = curr;  // Move prev to the current node
    }
    
    return head; // Return the head of the DLL
}


//TODO: this function is to print the Linked LIst.
void print_list(Node* head){
  while(head){
    cout <<head->data << " ";
    head = head->next;
  }
  cout << endl;
}



//NOTE: this is the function that reverses a DLL. so the concept is this :
//start from the head, copy it to curr.
Node* reverse_DLL(Node* head){
  if(!head) return nullptr; //NOTE: if the head itself is nullptr we return nullptr as well.

  Node* temp = nullptr; //NOTE: this is a temporary pointer used to swap the prev and next pointers.
  Node* curr = head; //NOTE: this is a pointer used to traverse the linked list.
  while(curr){ //TODO: loop runs until the curr is nullptr
    temp = curr->prev; //TODO: temp hold the prev node of the straight linked list.
    curr->prev = curr->next; //TODO: we are swapping the values of the prev and next here.
    curr->next = temp; //TODO: just assigning the value present in the temporary pointer.
    curr = curr->prev; //TODO: since our next has become prev now, we assign curr = curr->prev instead of curr = curr->next;
  }
  //NOTE: a tricky part is that temp will be pointing to the second last node at the end of everything, when curr has become nullptr. so we should return tmep->prev if temp exists in the first place.
  return temp->prev;
}





int main(){

  vector<int> arr{1,2,3,4,5,6,7,8};
  Node* head = convertARR2DLL(arr);
  Node* temp = head;
  cout << "The linked list from array : " << endl;
  print_list(temp); 
  cout << "After Reversing a DLL: " << endl;
  Node* temp2 = reverse_DLL(head);
  print_list(temp2);

  return 0;
}
