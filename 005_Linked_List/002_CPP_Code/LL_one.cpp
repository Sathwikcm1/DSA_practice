#include<bits/stdc++.h>
using namespace std;
//FIXME: this is using the struct keyword instead of using class keyword.
struct Node {
  /*public: */
    int data;
    Node* next;
  /*public: */
    Node(int data1, Node* next1){
      data = data1;
      next = next1;
    }
    Node(int data1){ //this is just an extra constructor.
      data = data1;
      next = nullptr;
    } 
};

//TODO: we don't need to define public since by default struct is public. 

int main(){
  cout << "Finally reached Linked list." << endl;
  vector<int> arr{2,4,5,6,7};
  int n = arr.size();
  Node* y = new Node(arr[0], nullptr); //TODO:: we are creating a pointer here. we can print the pointer itself which would display the memory location.
  cout << y->next << endl;  //TODO: we are -> operator because it is a pointer not an object. we . operator when we are dealing with an object directly not a pointer.
  cout << y << endl;
  return 0;
}
