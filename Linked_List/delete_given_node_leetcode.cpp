//FIXME: In this question we are given a node, we have to delete that given node.
//the problem is that we are not given the head for this question, just the node itself.
//so we cannot access the previous element.

#include<bits/stdc++.h>
using namespace std;

class Node{
  public: 
    int data;
    Node* next;

    Node(int data1, Node* next1){
      data = data1;
      next = next1;
    }

    Node(int data1){
      data = data1;
      next = nullptr;
    }
};


void delete_node(Node* node){
 if(node == nullptr || node->next == nullptr) return;

 node->data = node->next->data;
 Node* temp = node->next;
 node->next = node->next->next;
 delete temp;
}


void printList(Node* head){
  while(head){
    cout << head->data << " ";
    head = head->next;
  }
  cout << endl;
}


int main(){


    Node* head = new Node(4);
    head->next = new Node(5);
    head->next->next = new Node(1);
    head->next->next->next = new Node(9);
    cout << "The original Linked List: \n";
    printList(head);
    Node* given_node = head->next;
    delete_node(given_node);
    cout << "The list after deleting the given node. "<< endl;
    printList(head);
  return 0;
}
