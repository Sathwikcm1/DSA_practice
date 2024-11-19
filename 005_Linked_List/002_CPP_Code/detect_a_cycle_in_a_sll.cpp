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

bool brute_force_approach(Node* head){
  Node* temp = head;
  map<Node*,int> mp;
  //TODO: unordered maps and maps, unordered maps has O(1) as the avg time complexity compared to O(logn). But the worst case time complexity is O(n) whereas maps has O(logn).
  //so let's just map here, because of me RCB luck.
  while(temp){
    if(mp.find(temp) != mp.end()){
      return true;
    }
    mp[temp] = 1;
    temp = temp->next;
  }
  return false;
}

bool optimal_approach(Node* head){
  Node* slow = head;
  Node* fast = head;

  while(fast != nullptr || fast->next != nullptr){
    slow = slow->next;
    fast = fast->next->next;
    if(fast == slow) return true;
  }
  return false;
}

int main(){

    Node* head = new Node(1);
    Node* second = new Node(2);
    Node* third = new Node(3);
    Node* fourth = new Node(4);
    Node* fifth = new Node(5);

    head->next = second;
    second->next = third;
    third->next = fourth;
    fourth->next = fifth;
     // Create a loop
    fifth->next = third; 
    if(brute_force_approach(head)){
      cout << "There is a loop present in the linked list." << endl;
    }
    else{
      cout << "There is no loop present in the given linked list." << endl;
    }
    if(optimal_approach(head)){
      cout <<" A loop is present. tortoise and hare approach." << endl;
    }else{
      cout << " NO loop is present. " << endl;
    }
  return 0;
}
