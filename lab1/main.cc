#include "priority_queue.h"

//  int, double, string, vector, book, character, series

bool comparatorInt(const int& a, const int& b) { return a > b; }
bool comparatorDouble(const double& a, const double& b) { return a > b; }
bool comparatorChar(const char& a, const char& b) { return a > b; }
bool comparatorString(const std::string& a, const std::string& b) {
  return a.length() > b.length();
}
bool comparatorVector(const std::vector<int>& a, const std::vector<int>& b) {
  return a.size() > b.size();
}
bool comparatorBook(const mybook::Book& a, const mybook::Book& b) {
  return a.GetYear() > b.GetYear();
}
bool comparatorCharacter(const mybook::Character& a,
                         const mybook::Character& b) {
  return a.AmountOfBooksWhereCharacterIsPresent() >
         b.AmountOfBooksWhereCharacterIsPresent();
}
bool comparatorSeries(const mybook::Series& a, const mybook::Series& b) {
  return a.AmountOfBooks() > b.AmountOfBooks();
}

int main() {
  std::vector<int> arr;
  for (int i = 0; i < 10; i++) {
    arr.push_back(std::rand() % 40 + 1);
  }
  std::vector<int> arr1;
  for (int i = 0; i < 10; i++) {
    arr1.push_back(std::rand() % 40 + 20);
  }
  std::vector<int> arr2;
  for (int i = 0; i < 10; i++) {
    arr2.push_back(std::rand() % 40 + 30);
  }
  mypriorityqueue::Priority_queue_binary_tree<std::vector<int>> priorityQueue(
      comparatorVector);
  priorityQueue.Enqueue(arr);
  priorityQueue.Enqueue(arr1);
  priorityQueue.Enqueue(arr2);
  priorityQueue.Print();
  // fix binary tree enqueue or inorderTraversal methods
  //    priorityQueue.Dequeue();
  std::cout << priorityQueue.GetSize() << " size.\n";
  //   std::cout << priorityQueue.Peek();
}