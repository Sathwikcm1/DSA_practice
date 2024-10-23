//FIXME: this question is about return the mid node of the Linked list. we have to return the node itself not the value.
//so the return type is also node*.
#include<bits/stdc++.h>
using namespace std;

class Node{
  public: 
    int data;
    Node* next;

    Node(int data1, Node* next1 = nullptr){
      data = data1;
      next = next1;
    }
};


//NOTE: this is the brute force solution, in this we traverse the LL two times.
//first if the ll has no node or linked list only one node we return nullptr or head respectively.
//and then we go through the LL counting the number of nodes present.
//if there are odd number of nodes present we will return the mid element easemony, otherwise we return the second mid element in case of even.
Node* brute_force(Node* head){
  //TODO: in total time complexity: O(n/2 + n). and space complexity is O(1).
  Node* temp = head;
  if(head == nullptr || head->next == nullptr) return head;
  
  int cnt = 0;
  while(temp){ //TODO: this will take O(N) time complexity.
    cnt++;
    temp = temp->next;
  }
  //TODO: in case of even , ex: if n is 5, 5/2 + 1 = 3 orrr if n = 6, 6/2 + 1 = 4 , which is exactly what we want to return.
  int mid = (cnt/2) + 1;
  //TODO: we just have our mid element index now.
  temp = head;
  //TODO: this will take O(n/2) time complexity.
  while(temp){ //TODO: as we traverse we subtract mid one by one , when mid becomes zero we have our element. we break out of the loop.
    mid -= 1;
    if(mid == 0) break;
    temp = temp->next;
  }
  //TODO: then we return the temp element.
  return temp;
}


//NOTE: this algo is called Tortoise and Hare algorithm.
//this is simple intuitation, when one pointer moves n distance, the slow pointer will be moving n/2 distance.
//Now the time complexity 
Node* optimal_approach(Node* head){
  Node* slow = head;
  Node* fast = head;
  //NOTE: the reason we write fast!=nullptr and fast->next!= nullptr is because the linked list can be even or odd.
  //if it is odd the fast->next will work as fast will be pointing to the last second before it becomes the nullptr itself.
  while(fast != nullptr && fast->next != nullptr){
   slow = slow->next;
   fast = fast->next->next;
  }
  return slow;
  //NOTE: if slow is moving x/2 distance and fast is moving x distance , if there is a loop they will collide at some upcoming position.
  //NOTE: can also return fast, cuz both will be pointing to the same node.
}



int main(){
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);

    // Find the middle node
    Node* middleNode = brute_force(head);

    // Display the value of the middle node
    cout << "The middle node value is: " << middleNode->data << endl;

    Node* middleNode2 = optimal_approach(head);
    cout << "The middle Node value using optimal_approach: " <<  middleNode2->data << endl;
  return 0;
}
