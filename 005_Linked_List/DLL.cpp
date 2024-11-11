//FIXME: DLL: Double Linked List, it is basically singly linked list but you can travel backwards also. 
//instead containing one pointer in the node, it will now contain two pointers, one is obviously next and another one is prev pointing to the previous node.
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

int main(){
  vector<int> arr{1,2,3,4,4,5,6};
  Node* head = convert_arr_DLL(arr);
  Node* temp = head;
  while(temp){
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
  return 0;
}
