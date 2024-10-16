#include<bits/stdc++.h>
using namespace std;
//TODO: this is using class instead of using the struct keyword like before. here we can get 
//inheritance and all the oops benefits when we use the class keyword we have to specify 
//the public part and the private part as well.
class Node{
  public:
  int data;
  Node* next;

  public: 
  Node(int data1, Node* next1){
    data = data1;
    next = next1;
  }
  public: 
  Node(int data1){
    data = data1;
    next = nullptr;
  }
};

//NOTE: function to convert an array into a linked list.
Node* convertArr2LL(vector<int> &arr){
  Node* head = new Node(arr[0]); ///the second constructor in work here.
  Node* mover = head;
  //TODO: mover pointer is used as a temp pointer in order to move to the next node.
  int n = arr.size();
  for(int i = 1 ; i < n ; i++){
    Node* temp = new Node(arr[i]);
    mover->next = temp;
    mover = temp;
  }
  return head;
}

//NOTE: function to find out the length of a linked list.
//Time complexity is O(N) where N is the elements present inside the linked list.
int lengthofLL(Node *head){
  int cnt = 0;
  Node* temp = head;
  while(temp){
    cnt++; 
    temp = temp->next;
  }
  return cnt;
}

//NOTE: search if an element is present in the given linked list.
int search(Node* head, int val){
  Node* temp = head;
  while(temp){
    if(temp->data == val) return 1; 
    temp = temp->next;
  }
  return 0;
}

int main(){
  vector<int> arr = {4,5,5,7,8,9};
  Node* head = convertArr2LL(arr);
  //TODO: Traversing a Linked list: create a temp pointer.
  //FIXME: DO NOT TAMPER WITH THE HEAD POINTER.
  //TODO: make a reference of it. use that instead.
  Node* temp = head;
  while(temp){ //NOTE: as long as the temp is not equal to NULL which basically means that every single element has been printed.
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
  int l = lengthofLL(head);
  cout << "The length of the Linked List is " << l << " ." << endl;
  if(search(head,7)){
    cout << "The search was successful, The element is found." << endl;
  }
  return 0;
}
