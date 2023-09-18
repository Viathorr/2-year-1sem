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
};

template <class T>
class Priority_queue_linked_list : public Priority_queue<T> {
 public:
  Priority_queue_linked_list(
      std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator){};
  void Enqueue(T data) override {}
  void Dequeue() override {}
  T Peek() override {}
  int GetSize() override {}

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
  void Enqueue(T data) override {}
  void Dequeue() override {}
  T Peek() override {}
  int GetSize() override {}

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

  void Enqueue(T data) override;
  void Dequeue() override;
  T Peek() override;
  int GetSize() override;

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
  void Enqueue(T data) override {}
  void Dequeue() override {}
  T Peek() override {}
  int GetSize() override {}

 private:
  std::function<bool(const T&, const T&)> comparator;
  vector<T> queue;
  void Bubble_up(int index) {}
  void Bubble_down(int index) {}
  int FindParent(int index) {}
  int FindLeftChild(int index) {}
};
}  // namespace mypriorityqueue

#endif