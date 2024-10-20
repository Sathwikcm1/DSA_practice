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
  return 0;
}
