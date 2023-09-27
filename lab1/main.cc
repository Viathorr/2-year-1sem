#include "comparator.h"
#include "priority_queue.h"

void checkInt(mypriorityqueue::Priority_queue<int> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(myrandomdatagenerator::Random_data_generator::GetRandomIntData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

void checkDouble(mypriorityqueue::Priority_queue<double> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomDoubleData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

void checkChar(mypriorityqueue::Priority_queue<char> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomCharData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

void checkString(mypriorityqueue::Priority_queue<std::string> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomStringData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

template <typename T>
void checkVector(mypriorityqueue::Priority_queue<std::vector<T>> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomVectorData<T>());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

void checkBook(mypriorityqueue::Priority_queue<mybook::Book> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomBookData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

void checkBook(mypriorityqueue::Priority_queue<mybook::Character> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomCharacterData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

void checkSeries(mypriorityqueue::Priority_queue<mybook::Series> &q) {
  q.GenerateRandomData();
  std::cout << "PQ size: " << q.GetSize() << ", data: \n";
  q.Print();
  for (int i = 0; i < 3; i++) {
    q.Enqueue(
        myrandomdatagenerator::Random_data_generator::GetRandomSeriesData());
  }
  std::cout << "Peek: " << q.Peek()
            << ", size after 3 insertions: " << q.GetSize()
            << ", data: " << std::endl;
  q.Print();
  for (int i = 0; i < 4; i++) {
    q.Dequeue();
  }
  std::cout << "PQ size after 4 removals: " << q.GetSize()
            << ", peek: " << q.Peek() << std::endl;
}

int main() {
  srand(time(NULL));

  std::cout << "\n~~~ Priority queue implemented by linked list: \n\n";
  mypriorityqueue::Priority_queue_linked_list<mybook::Book> PQ(
      mycomparator::comparatorBook);
  checkBook(PQ);

  std::cout << "\n~~~ Priority queue implemented by array: \n\n";
  mypriorityqueue::Priority_queue_array<mybook::Book> PQ1(
      mycomparator::comparatorBook);
  checkBook(PQ1);

  std::cout << "\n~~~ Priority queue implemented by binary heap: \n\n";
  mypriorityqueue::Priority_queue_binary_heap<mybook::Book> PQ2(
      mycomparator::comparatorBook);
  checkBook(PQ2);

  std::cout << "\n~~~ Priority queue implemented by binary (search) tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<mybook::Book> PQ3(
      mycomparator::comparatorBook);
  checkBook(PQ3);

  std::cout << "\n~~~ Priority queue implemented by AVL tree: \n\n";
  mypriorityqueue::Priority_queue_AVL_tree<mybook::Book> PQ4(
      mycomparator::comparatorBook);
  checkBook(PQ4);

  return 0;
}