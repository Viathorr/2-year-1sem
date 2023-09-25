#include "comparator.h"
#include "priority_queue.h"

//  int, double, string, vector, book, character, series

int main() {
  srand(time(NULL));
  std::cout << "\n~~~ Priority queue implemented by linked list: \n\n";
  mypriorityqueue::Priority_queue_linked_list<int> intPQ(
      mycomparator::comparatorInt);
  intPQ.GenerateRandomData();
  std::cout << "PQ size: " << intPQ.GetSize() << ", data: \n";
  intPQ.Print();
  intPQ.Enqueue(23);
  intPQ.Enqueue(109);
  intPQ.Enqueue(1);
  std::cout << "Peek: " << intPQ.Peek()
            << ", size after 3 insertions: " << intPQ.GetSize()
            << ", data: " << std::endl;
  intPQ.Print();
  intPQ.Dequeue();
  intPQ.Dequeue();
  intPQ.Dequeue();
  intPQ.Dequeue();
  std::cout << "PQ size after 4 removals: " << intPQ.GetSize() << ", data: \n";
  intPQ.Print();

  std::cout << "\n~~~ Priority queue implemented by array: \n\n";
  mypriorityqueue::Priority_queue_array<int> intPQ1(
      mycomparator::comparatorInt);
  intPQ1.GenerateRandomData();
  std::cout << "PQ size: " << intPQ1.GetSize() << ", data: \n";
  intPQ1.Print();
  intPQ1.Enqueue(23);
  intPQ1.Enqueue(109);
  intPQ1.Enqueue(1);
  std::cout << "Peek: " << intPQ1.Peek()
            << ", size after 3 insertions: " << intPQ1.GetSize()
            << ", data: " << std::endl;
  intPQ1.Print();
  intPQ1.Dequeue();
  intPQ1.Dequeue();
  intPQ1.Dequeue();
  intPQ1.Dequeue();
  std::cout << "PQ size after 4 removals: " << intPQ1.GetSize() << ", data: \n";
  intPQ1.Print();

  std::cout << "\n~~~ Priority queue implemented by binary heap: \n\n";
  mypriorityqueue::Priority_queue_binary_heap<int> intPQ2(
      mycomparator::comparatorInt);
  intPQ2.GenerateRandomData();
  std::cout << "PQ size: " << intPQ2.GetSize() << ", data: \n";
  intPQ2.Print();
  intPQ2.Enqueue(23);
  intPQ2.Enqueue(109);
  intPQ2.Enqueue(1);
  std::cout << "Peek: " << intPQ2.Peek()
            << ", size after 3 insertions: " << intPQ2.GetSize()
            << ", data: " << std::endl;
  intPQ2.Print();
  intPQ2.Dequeue();
  intPQ2.Dequeue();
  intPQ2.Dequeue();
  intPQ2.Dequeue();
  std::cout << "PQ size after 4 removals: " << intPQ2.GetSize() << ", data: \n";
  intPQ2.Print();

  std::cout << "\n~~~ Priority queue implemented by binary (search) tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<int> intPQ3(
      mycomparator::comparatorInt);
  intPQ3.GenerateRandomData();
  std::cout << "PQ size: " << intPQ3.GetSize() << ", data: \n";
  intPQ3.Print();
  intPQ3.Enqueue(23);
  intPQ3.Enqueue(109);
  intPQ3.Enqueue(1);
  std::cout << "Peek: " << intPQ3.Peek()
            << ", size after 3 insertions: " << intPQ3.GetSize()
            << ", data: " << std::endl;
  intPQ3.Print();
  intPQ3.Dequeue();
  intPQ3.Dequeue();
  intPQ3.Dequeue();
  intPQ3.Dequeue();
  std::cout << "PQ size after 4 removals: " << intPQ3.GetSize() << ", data: \n";
  intPQ3.Print();

  std::cout << "\n~~~ Priority queue implemented by AVL tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<int> intPQ4(
      mycomparator::comparatorInt);
  intPQ4.GenerateRandomData();
  std::cout << "PQ size: " << intPQ4.GetSize() << ", data: \n";
  intPQ4.Print();
  intPQ4.Enqueue(23);
  intPQ4.Enqueue(109);
  intPQ4.Enqueue(1);
  std::cout << "Peek: " << intPQ4.Peek()
            << ", size after 3 insertions: " << intPQ4.GetSize()
            << ", data: " << std::endl;
  intPQ4.Print();
  intPQ4.Dequeue();
  intPQ4.Dequeue();
  intPQ4.Dequeue();
  intPQ4.Dequeue();
  std::cout << "PQ size after 4 removals: " << intPQ4.GetSize() << ", data: \n";
  intPQ4.Print();
  return 0;
}