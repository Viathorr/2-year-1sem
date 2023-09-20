#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <functional>
#include <memory>
#include <stdexcept>

namespace mypriorityqueue {
template <class T>
class Priority_queue  // priority queue interface
{
 public:
  virtual void Enqueue(T data) = 0;
  virtual void Dequeue() = 0;
  virtual T Peek() = 0;
  virtual int GetSize() = 0;
  virtual Print() = 0;
};

template <class T>
class Priority_queue_linked_list : public Priority_queue<T> {
 public:
  Priority_queue_linked_list(
      std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator){};
  void Enqueue(T data) override {
    std::unique_ptr<Priority_queue_linked_list<T>::Node> newNode =
        std::make_unique<Priority_queue_linked_list<T>::Node>(data);

    if (!head || comparator(data, head->data)) {
      newNode->next = std::move(head);
      head = std::move(newNode);
    } else {
      Priority_queue_linked_list<T>::Node* current = head.get();
      while (current->next && comparator(current->next->data, data)) {
        current = current->next.get();
      }
      newNode->next = std::move(current->next);
      current->next = std::move(newNode);
    }
  }
  void Dequeue() override {
    if (head) {
      head = std::move(head->next);
      --size;
    }
  }
  T Peek() override {
    if (head != nullptr)
      return head->data;
    else
      throw std::runtime_error("The queue is empty.");
  }
  int GetSize() override {
    if (size > 0)
      return size;
    else
      return 0;
  }
  void Print() override {
    if (!head)
      return;
    else {
      Node* currentNode = head.get();
      while (currentNode) {
        std::cout << currentNode->data << " \n";
        currentNode = currentNode->next.get();
      }
    }
    std::cout << std::endl;
  }

 private:
  std::function<bool(const T&, const T&)> comparator;
  class Node {
   public:
    Node();
    Node(T value) : data(value), next(nullptr){};
    T data;
    std::unique_ptr<Node> next;
  };
  std::unique_ptr<Node> head;
  int size;
};

template <class T>
class Priority_queue_array : public Priority_queue<T> {
 public:
  Priority_queue_array(std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator){};
  void Enqueue(T data) override {
    if (!queue.size() || comparator(data, queue.back()))
      queue.push_back(data);
    else {
      for (int i = 0; i < queue.size(); i++) {
        if (comparator(queue[i], data)) {
          queue.insert(queue.begin() + i, data);
          return;
        }
      }
    }
  }
  void Dequeue() override {
    if (!queue.size()) {
      throw std::runtime_error("The queue is empty.");
    } else {
      queue.pop_back();
    }
  }
  T Peek() override {
    if (!queue.empty()) {
      return queue.back();
    } else {
      throw std::runtime_error("The queue is empty.");
    }
  }
  int GetSize() override { return queue.size(); }
  void Print() override {
    for (int i = 0; i < queue.size(); i++) {
      std::cout << queue[i] << " \n";
    }
    std::cout << std::endl;
  }

 private:
  std::function<bool(const T&, const T&)> comparator;
  std::vector<T> queue;
};

template <class T>
class Priority_queue_binary_tree : public Priority_queue<T> {
 public:
  Priority_queue_binary_tree(
      std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator){};

  void Enqueue(T data) override {}
  void Dequeue() override {}
  T Peek() override {}
  int GetSize() override {}
  void Print() override {}

 private:
  std::function<bool(const T&, const T&)> comparator;
  class TreeNode {
   public:
    TreeNode();
    TreeNode(T value)
        : data(value), left(nullptr), right(nullptr), parent(nullptr){};
    T data;
    std::shared_ptr<TreeNode> left;
    std::shared_ptr<TreeNode> right;
    std::shared_ptr<TreeNode> parent;
  };
  std::shared_ptr<TreeNode> root;
  int size;
  void Bubble_up(std::shared_ptr<TreeNode> root);
  void Bubble_down(std::shared_ptr<TreeNode> root);
};

template <class T>
class Priority_queue_AVL_tree : public Priority_queue<T> {
 public:
  Priority_queue_AVL_tree(std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator) {}
  void Enqueue(T data) override {}
  void Dequeue() override {}
  T Peek() override {}
  int GetSize() override {}

 private:
  std::function<bool(const T&, const T&)> comparator;
  class TreeNode {
   public:
    TreeNode();
    TreeNode(T value) : data(value), left(nullptr), right(nullptr){};
    T data;
    std::shared_ptr<TreeNode> left;
    std::shared_ptr<TreeNode> right;
    int height;
  };
  std::shared_ptr<TreeNode> root;
  int size;
  int H(std::shared_ptr<TreeNode> root) {}
  int GetBalance(std::shared_ptr<TreeNode> root) {}
  std::shared_ptr<TreeNode> RotateLeft(std::shared_ptr<TreeNode> root) {}
  std::shared_ptr<TreeNode> RotateRight(std::shared_ptr<TreeNode> root) {}
};

template <class T>
class Priority_queue_binary_heap : public Priority_queue<T> {
 public:
  Priority_queue_binary_heap(
      std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator){};
  void Enqueue(T data) override {
    queue.push_back(data);
    Bubble_up(queue.size() - 1);
  }
  void Dequeue() override {
    if (queue.empty()) {
      throw std::runtime_error("The queue is empty.");
    } else {
      std::swap(queue.front(), queue.back());
      queue.pop_back();
      Bubble_down(0);
    }
  }
  T Peek() override {
    if (!queue.empty()) {
      return queue.front();
    } else {
      throw std::runtime_error("The queue is empty.");
    }
  }
  int GetSize() override { return queue.size(); }
  void Print() override {
    if (!queue.size()) {
      std::cout << "Queue is empty.\n";
    } else {
      int level = 0, levelSize = 1;
      while (level < queue.size()) {
        for (int i = level; i < level + levelSize && i < queue.size(); i++) {
          std::cout << queue[i] << " \n";
        }
        level += levelSize;
        levelSize *= 2;
      }
    }
  }

 private:
  std::function<bool(const T&, const T&)> comparator;
  vector<T> queue;
  void Bubble_up(int index) {
    if (FindParent(index) == -1) return;
    if (comparator(queue[index], queue[FindParent(index)])) {
      std::swap(queue[index], queue[FindParent(index)]);
      Bubble_up(FindParent(index));
    }
  }
  void Bubble_down(int index) {
    int higherPriorityElementIndex = index;
    int leftChild = FindLeftChild(index);

    for (int i = 0; i < 2; i++) {
      if (leftChild + i < queue.size()) {
        if (comparator(queue[leftChild + i],
                       queue[higherPriorityElementIndex])) {
          higherPriorityElementIndex = leftChild + i;
        }
      }
    }
    if (higherPriorityElementIndex != index) {
      std::swap(queue[index], queue[higherPriorityElementIndex]);
      Bubble_down(higherPriorityElementIndex);
    }
  }
  int FindParent(int index) { return !index ? (-1) : (index / 2); }
  int FindLeftChild(int index) { return (2 * index) + 1; }
};
}  // namespace mypriorityqueue

#endif