#include "comparator.h"
#include "priority_queue.h"

//  int, double, string, vector, book, character, series

int main() {
  srand(time(NULL));
  mypriorityqueue::Priority_queue_binary_tree<std::vector<double>>
      priorityQueue(mycomparator::comparatorVector<double>);
  priorityQueue.GenerateRandomData();

  priorityQueue.Print();
  std::cout << priorityQueue.GetSize() << " size.\n";
}