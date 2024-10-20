#include<bits/stdc++.h>
using namespace std;

class Node{
  public:
    int data;
    Node* prev;
    Node* next;

    Node(int data1, Node* prev1 = nullptr,Node* next1 = nullptr ){
      data = data1;
      prev= prev1;
      next = next1;
    }
};




//TODO: this function basicallay converts an array into a DLL.
Node* convertARR2DLL(vector<int> &arr){
  Node* head = new Node(arr[0],nullptr,nullptr);
  Node* prev =head;
  for(size_t i = 1; i < arr.size(); i++){
    Node* curr = new Node(arr[i],prev,nullptr);
    prev->next = curr;
    prev = curr;
  }
  return head;
}



//TODO: Add the head, cases no node is present simply return the new node. and the rest is just create a new node, make the next of the curr point to the curr head, and the prev of the current head to the curr node.
//and then ww return the current node as the head.
Node* insert_Head(Node* head,int val){
  if(head == nullptr){
    return new Node(val,nullptr,nullptr);
  }

  Node* new_Head = new Node(val,nullptr,head);
  head->prev = new_Head;
  return new_Head;
}




//TODO: This is for inserting a new Tail.
//Cases, if there no linked list, it should return a new node as head. if there is linked list. then we need to traverse until curr->next == nullptr. and then we need
//to make the curr->next point to the new node and then we should make the new_node->prev to point to the curr node.
Node* insert_Tail(Node* head, int val){
  if(head == nullptr) return new Node(val,nullptr,nullptr);

  Node* curr = head;
  while(curr->next){
    curr = curr->next;
  }

  Node* new_Node = new Node(val,curr,nullptr);
  curr->next=new_Node;
  return head;
}


//TODO: Insert a node at Kth position.
// i failed. dies
//
Node* insert_at_k(Node* head,int val,int k){
  if(head == nullptr) return new Node(val); //NOTE: this is the case if there is no linked list present, just return the new node.

  int cnt = 0;
  Node* curr = head;
  while(curr){
    cnt++;
    if(cnt == k-1) break;
    curr = curr->next;
  }

  //NOTE: if not, we are at the kth position now, curr is pointing to the k-1 node. 
  //so the current node would be pointing to the node right before the kth node. that is k -1 , so we need to add the new node after the current node. before that let's mark the kth node as next_Node.
  
  Node* new_Node = new Node(val,curr,curr->next);
  Node* next_Node = curr->next; //NOTE: creating  a new node to point to the next_Node of the current node.
  next_Node -> prev = new_Node;
  curr->next = new_Node;
  return head;
}





//TODO: this function is to print the Linked LIst.
void print_list(Node* head){
  while(head){
    cout <<head->data << " ";
    head = head->next;
  }
  cout << endl;
}





int main(){
  vector<int> arr{1,2,3,4,5,6,7,8};
  Node* head = convertARR2DLL(arr);
  Node* temp = head;
  cout << "The linked list from array : " << endl;
  print_list(temp); 


  cout << "Inserting 500 as the new Head." << endl;
  head = insert_Head(head,500);
  print_list(head);


  cout << "Inserting the 100 as the tail." << endl;
  head = insert_Tail(head,100);
  print_list(head);
  

  cout << "Inserting 50 at k = 4 position." << endl;
  head = insert_at_k(head,50,4);
  print_list(head);
  return 0;
}
