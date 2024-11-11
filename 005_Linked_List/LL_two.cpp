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

int main(){
  vector<int> arr = {4,5,5,7,8,9};
  Node* s = new Node(arr[0]);
  cout << s->data << endl;
  cout << s->next << endl;
  cout << s << endl;
  //NOTE: new keyword is used to dynamically allocate the memory to that object.
  return 0;
}
