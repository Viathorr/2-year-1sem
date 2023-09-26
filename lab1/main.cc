#include "comparator.h"
#include "priority_queue.h"

//  int, double, string, vector, book, character, series

int main() {
  srand(time(NULL));

  std::cout << "\n~~~ Priority queue implemented by linked list: \n\n";
  mypriorityqueue::Priority_queue_linked_list<mybook::Book> bookPQ(
      mycomparator::comparatorBook);
  bookPQ.GenerateRandomData();
  std::cout << "PQ size: " << bookPQ.GetSize() << ", data: \n";
  bookPQ.Print();
  bookPQ.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  std::cout << "Peek: " << bookPQ.Peek()
            << ", size after 3 insertions: " << bookPQ.GetSize()
            << ", data: " << std::endl;
  bookPQ.Print();
  bookPQ.Dequeue();
  bookPQ.Dequeue();
  bookPQ.Dequeue();
  bookPQ.Dequeue();
  std::cout << "PQ size after 4 removals: " << bookPQ.GetSize() << ", data: \n";
  bookPQ.Print();

  std::cout << "\n~~~ Priority queue implemented by array: \n\n";
  mypriorityqueue::Priority_queue_array<mybook::Book> bookPQ1(
      mycomparator::comparatorBook);
  bookPQ1.GenerateRandomData();
  std::cout << "PQ size: " << bookPQ1.GetSize() << ", data: \n";
  bookPQ1.Print();
  bookPQ1.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ1.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ1.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  std::cout << "Peek: " << bookPQ1.Peek()
            << ", size after 3 insertions: " << bookPQ1.GetSize()
            << ", data: " << std::endl;
  bookPQ1.Print();
  bookPQ1.Dequeue();
  bookPQ1.Dequeue();
  bookPQ1.Dequeue();
  bookPQ1.Dequeue();
  std::cout << "PQ size after 4 removals: " << bookPQ1.GetSize()
            << ", data: \n";
  bookPQ1.Print();

  std::cout << "\n~~~ Priority queue implemented by binary heap: \n\n";
  mypriorityqueue::Priority_queue_binary_heap<mybook::Book> bookPQ2(
      mycomparator::comparatorBook);
  bookPQ2.GenerateRandomData();
  std::cout << "PQ size: " << bookPQ2.GetSize() << ", data: \n";
  bookPQ2.Print();
  bookPQ2.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ2.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ2.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  std::cout << "Peek: " << bookPQ2.Peek()
            << ", size after 3 insertions: " << bookPQ2.GetSize()
            << ", data: " << std::endl;
  bookPQ2.Print();
  bookPQ2.Dequeue();
  bookPQ2.Dequeue();
  bookPQ2.Dequeue();
  bookPQ2.Dequeue();
  std::cout << "PQ size after 4 removals: " << bookPQ2.GetSize()
            << ", data: \n";
  bookPQ2.Print();

  std::cout << "\n~~~ Priority queue implemented by binary (search) tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<mybook::Book> bookPQ3(
      mycomparator::comparatorBook);
  bookPQ3.GenerateRandomData();
  std::cout << "PQ size: " << bookPQ3.GetSize() << ", data: \n";
  bookPQ3.Print();
  bookPQ3.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ3.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ3.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  std::cout << "Peek: " << bookPQ3.Peek()
            << ", size after 3 insertions: " << bookPQ3.GetSize()
            << ", data: " << std::endl;
  bookPQ3.Print();
  bookPQ3.Dequeue();
  bookPQ3.Dequeue();
  bookPQ3.Dequeue();
  bookPQ3.Dequeue();
  std::cout << "PQ size after 4 removals: " << bookPQ3.GetSize()
            << ", data: \n";
  bookPQ3.Print();

  std::cout << "\n~~~ Priority queue implemented by AVL tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<mybook::Book> bookPQ4(
      mycomparator::comparatorBook);
  bookPQ4.GenerateRandomData();
  std::cout << "PQ size: " << bookPQ4.GetSize() << ", data: \n";
  bookPQ4.Print();
  bookPQ4.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ4.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  bookPQ4.Enqueue(
      myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  std::cout << "Peek: " << bookPQ4.Peek()
            << ", size after 3 insertions: " << bookPQ4.GetSize()
            << ", data: " << std::endl;
  bookPQ4.Print();
  bookPQ4.Dequeue();
  bookPQ4.Dequeue();
  bookPQ4.Dequeue();
  bookPQ4.Dequeue();
  std::cout << "PQ size after 4 removals: " << bookPQ4.GetSize()
            << ", data: \n";
  bookPQ4.Print();

  return 0;
}