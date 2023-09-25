#include "comparator.h"
#include "priority_queue.h"

//  int, double, string, vector, book, character, series

int main() {
  srand(time(NULL));

  std::cout << "\n~~~ Priority queue implemented by linked list: \n\n";
  mypriorityqueue::Priority_queue_linked_list<std::vector<int>> vectorPQ(
      mycomparator::comparatorVector<int>);
  vectorPQ.GenerateRandomData();
  std::cout << "PQ size: " << vectorPQ.GetSize() << ", data: \n";
  vectorPQ.Print();
  vectorPQ.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  std::cout << "Peek: " << vectorPQ.Peek()
            << ", size after 3 insertions: " << vectorPQ.GetSize()
            << ", data: " << std::endl;
  vectorPQ.Print();
  vectorPQ.Dequeue();
  vectorPQ.Dequeue();
  vectorPQ.Dequeue();
  vectorPQ.Dequeue();
  std::cout << "PQ size after 4 removals: " << vectorPQ.GetSize()
            << ", data: \n";
  vectorPQ.Print();

  std::cout << "\n~~~ Priority queue implemented by array: \n\n";
  mypriorityqueue::Priority_queue_array<std::vector<int>> vectorPQ1(
      mycomparator::comparatorVector<int>);
  vectorPQ1.GenerateRandomData();
  std::cout << "PQ size: " << vectorPQ1.GetSize() << ", data: \n";
  vectorPQ1.Print();
  vectorPQ1.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ1.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ1.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  std::cout << "Peek: " << vectorPQ1.Peek()
            << ", size after 3 insertions: " << vectorPQ1.GetSize()
            << ", data: " << std::endl;
  vectorPQ1.Print();
  vectorPQ1.Dequeue();
  vectorPQ1.Dequeue();
  vectorPQ1.Dequeue();
  vectorPQ1.Dequeue();
  std::cout << "PQ size after 4 removals: " << vectorPQ1.GetSize()
            << ", data: \n";
  vectorPQ1.Print();

  std::cout << "\n~~~ Priority queue implemented by binary heap: \n\n";
  mypriorityqueue::Priority_queue_binary_heap<std::vector<int>> vectorPQ2(
      mycomparator::comparatorVector<int>);
  vectorPQ2.GenerateRandomData();
  std::cout << "PQ size: " << vectorPQ2.GetSize() << ", data: \n";
  vectorPQ2.Print();
  vectorPQ2.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ2.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ2.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  std::cout << "Peek: " << vectorPQ2.Peek()
            << ", size after 3 insertions: " << vectorPQ2.GetSize()
            << ", data: " << std::endl;
  vectorPQ2.Print();
  vectorPQ2.Dequeue();
  vectorPQ2.Dequeue();
  vectorPQ2.Dequeue();
  vectorPQ2.Dequeue();
  std::cout << "PQ size after 4 removals: " << vectorPQ2.GetSize()
            << ", data: \n";
  vectorPQ2.Print();

  std::cout << "\n~~~ Priority queue implemented by binary (search) tree:\n\n";
  mypriorityqueue::Priority_queue_AVL_tree<std::vector<int>> vectorPQ3(
      mycomparator::comparatorVector<int>);
  vectorPQ3.GenerateRandomData();
  std::cout << "PQ size: " << vectorPQ3.GetSize() << ", data: \n";
  vectorPQ3.Print();
  vectorPQ3.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ3.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ3.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  std::cout << "Peek: " << vectorPQ3.Peek()
            << ", size after 3 insertions: " << vectorPQ3.GetSize()
            << ", data: " << std::endl;
  vectorPQ3.Print();
  vectorPQ3.Dequeue();
  vectorPQ3.Dequeue();
  vectorPQ3.Dequeue();
  vectorPQ3.Dequeue();
  std::cout << "PQ size after 4 removals: " << vectorPQ3.GetSize()
            << ", data: \n";
  vectorPQ3.Print();

  std::cout << "\n~~~ Priority queue implemented by AVL tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<std::vector<int>> vectorPQ4(
      mycomparator::comparatorVector<int>);
  vectorPQ4.GenerateRandomData();
  std::cout << "PQ size: " << vectorPQ4.GetSize() << ", data: \n";
  vectorPQ4.Print();
  vectorPQ4.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ4.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  vectorPQ4.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomVectorData<int>());
  std::cout << "Peek: " << vectorPQ4.Peek()
            << ", size after 3 insertions: " << vectorPQ4.GetSize()
            << ", data: " << std::endl;
  vectorPQ4.Print();
  vectorPQ4.Dequeue();
  vectorPQ4.Dequeue();
  vectorPQ4.Dequeue();
  vectorPQ4.Dequeue();
  std::cout << "PQ size after 4 removals: " << vectorPQ4.GetSize()
            << ", data: \n";
  vectorPQ4.Print();
  return 0;
}