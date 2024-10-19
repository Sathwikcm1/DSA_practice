//FIXME: Insertion in Singly Linked list. inserting at the head,tail, in kth position, before the value k.
#include <bits/stdc++.h>

using namespace std;
//TODO: this is as usual defining the class and the constructors for the node creation.
class Node {
public:
    int data;
    Node* next;
public:
    Node(int data1, Node* next1) { //TODO: construcotr 1
        data = data1;
        next = next1;
    }
public:

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

//TODO: Insertion in Linked list.
//TODO: this is about adding the node to the front of the linked list, making the newer node as the head of the linked list.
Node* inserthead(Node* head, int val){
  Node* temp = new Node(val,head);
  return temp;
}
//TODO: that is it. it is that simple, just create a new node, and put the next of that node as head and return the temp.



//NOTE: Inserting at the last. this will take obviosuly o(n) time complexity.
Node* insert_at_end(Node* head, int val){
  if(head == nullptr){
    return new Node(val);
  }
  Node* temp = head;
  while(temp->next){
    temp = temp->next;
  }
  temp->next = new Node(val,nullptr);
  return head;
}


//NOTE: Insert at a position k.
//Note that k = (1-N+1) , so if n is 4, there are four nodes, either k can be 1 ,2,3,4, or even 5.
//note that the counting in linked list is normal like it goes 1,2,3 no it doesn't start from zero dumbass.
//if k is the given position for the new node to be inserted, we will insert a new node right before k.
Node* insert_at_pos(Node* head, int k, int val){
  if(head == nullptr){
    if(k == 1){ //TODO: this is here because we have to make sure the k is within the range other wise not to insert the node.
     return new Node(val);
    }
  }
  //TODO: A whole linked list already exists we just have to insert a node at the beginning before the existing head.
  if(k == 1){
    Node* new_head = new Node(val,head);
    return new_head;
  }

  //TODO: now is the case if it is somewhere in the middle of the nodes.
  int cnt = 0;
  Node* temp = head;
  while(temp){
    cnt++;
    if(cnt == k-1){
      Node* new_node = new Node(val,temp->next);
      temp->next = new_node;
      break;
    }
    temp=temp->next;
  } 
 return head; 
}


//NOTE: this is for inserting a node based on the value itself not the position.
//so we will be given el(10), and then we are given the node value 5, so we have to insert the node 10 right before the 5.
Node* insert_based_val(Node* head,int el, int val){
  if(head == nullptr){
    return nullptr;
  }

  if(head->data == val){
    Node* new_node = new Node(el,head);
    return new_node;
  }
  Node* temp = head;
  while(temp != nullptr){
    if(temp->data == val){
      Node* x = new Node(el,temp->next);
      temp-> next = x;
      break;
    }
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
    head = inserthead(head,10);
    Node* temp1 = head;
    cout << "The linked list after inserting a new head.\n"; 
    while (temp1) {
        cout << temp1->data << " ";
        temp1 = temp1->next;
    }
    cout << endl;
    cout << "Inserting at the end of the Linked List: ";
    head = insert_at_end(head,100);
    Node* temp2 = head;
    while (temp2) {
        cout << temp2->data << " ";
        temp2 = temp2->next;
    }
    cout << endl;
    cout << "Inserting at the 3rd position of the Linked list: 500 " << endl;
    head = insert_at_pos(head,3,500);
    Node* temp9 = head;
    while(temp9){
      cout << temp9->data << " ";
      temp9 = temp9->next;
    }
    cout << endl;
  return 0;
}
