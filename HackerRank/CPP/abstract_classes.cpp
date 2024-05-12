#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

class LRUCache : public Cache {
public:
LRUCache(int cap) { cp = cap; }

void set(int k, int v) {
    // 1. if key found, replace value and move key to front
    // 2. if key not found, add new key to front
    // 3. if over capacity, remove oldest key from back

    // 1. search for key
    // cout << "set" << endl;
    auto search = mp.find(k);
    if (search != mp.end()) {  // found the key, a hit!
        //cout << "hit! replace value and move key" << endl;
        Node *one = mp.at(k);
        Node *two = head;
        if (one->prev)
            one->prev->next = one->next;
        if (one->next)
            one->next->prev = one->prev;
        one->next = head;
        one->prev = NULL;
        head->next = two;
        head->prev = one;
        head = one;
        head->value = v;

    } else {   // 2. key not found, add new key to front
        // cout << "miss! adding new node " << k << " " << v << endl;
        Node *n = new Node(k, v);
        if (mp.size() == 0) {
            //cout << "size = 0" << endl;
            head = n;
            tail = n;
        } else if (mp.size() < cp) {
            //cout << "size < cp" << endl;
            head->prev = n;
            n->next = head;
            head = n;
        } else if (mp.size() >= cp) {
            //cout << "size >= cp" << endl;
            head->prev = n;
            n->next = head;
            head = n;
            tail->prev->next = NULL;
            int tmp = tail->key;
            mp.erase(tmp);
            tail = tail->prev;
        }
        mp.insert(pair<int,Node*>(k,n));
    }
}

int get(int key) { 
    auto search = mp.find(key);
    if (search != mp.end())   // found the key
        return search->second->value;  // return the value
    return -1;
}

};

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         //cout << "get " << key << " " << l.get(key) << endl;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         //cout << "set " << key << " " << value << endl;
         l.set(key,value);
      }
   }
   return 0;
}
