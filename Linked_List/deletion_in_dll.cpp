//FIXME: this is about deletion in dll. same operation we did in sll.
#include<bits/stdc++.h>
using namespace std;

class Node{
  public:
  int data;
  Node* next;
  Node* back;
  public:
  Node(int data1, Node* next1, Node* back1){
    data = data1;
    next = next1;
    back = back1;
  }
  public: 
  Node(int data1){
    data = data1;
    next = nullptr;
    back = nullptr;
  }
};


Node* convert_arr_DLL(vector<int> arr){
  Node* head = new Node(arr[0]);
  Node* prev = head; //TODO: this is the pointer that remembers the previous node do not get confused
                     //with the back, it is back in the constructor but here we represent that with the prev pointer.
  for(int i = 1 ; i < arr.size();i++){
    Node* temp = new Node(arr[i], nullptr , prev); //TODO: as it was told earlier prev is passed for back pointer, it is the same thing.
    prev->next = temp;
    prev = temp;
  }
  return head;
}



//NOTE: this about deleting the head of the given linked list.
//we need to check for cases here. for containing no nodes to containing one node , to containing
//many nodes.
Node* delete_head(Node* head){
  if(head == nullptr || head->next == nullptr ){ //TODO: if head is pointing to the nullptr or the next of the head is pointing to the nullptr 
                                                 //which means the LL is empty or only one node exists in both the cases we can just return a  nullptr.
    return nullptr;
  }
  //TODO: otherwise, we'll make a prev which is pointing to the head. then we move the head. we change the head's back to the null, and then we change the prev's next to nullptr
  //and then we delete the prev and return the head.
  Node* prev = head;
  head = head->next;
  head->back = nullptr;
  prev->next = nullptr;
  delete prev;
  return head;
}




//NOTE: this is about deleting the tail of the given linkedlists.
//cases if only one node exists or no node exists at all we just need to return the nullptr that is it. 
Node* delete_tail(Node* head){
  if(head == nullptr)
    return nullptr;
  if(head->next == nullptr){
    delete head;
    return nullptr;
  }
  Node* temp = head;
  while(temp->next != nullptr){

    temp = temp->next;
  }
  Node* prevNode = temp->back;
  prevNode->next = nullptr;
  temp->back = nullptr;
  delete temp;
  return head;
}



int main(){
  vector<int> arr{1,2,3,4,4,5,6};
  Node* head = convert_arr_DLL(arr);
  Node* temp = head;
  while(temp){
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
  cout << "After deleting the head of the LInked list." << endl;
  temp = delete_head(head);
  while(temp){
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
  cout << "After deleting the tail of the linked lists : "<< endl;
  temp = delete_tail(head);
  while(temp){
    cout << temp->data << " ";
    temp = temp->next;
  } 
  cout << endl;
  return 0;
}
