#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <functional>
#include <memory>
#include <stdexcept>

#include "randomDataGenerator.h"

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
    size++;
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

  void Enqueue(T data) override {
    if (!root) {
      root = std::make_shared<TreeNode>(data);
      the_highest_priority_node = root;
    } else {
      std::shared_ptr<TreeNode> new_node = std::make_shared<TreeNode>(data);
      if (comparator(data, the_highest_priority_node->data)) {
        the_highest_priority_node = new_node;
      }
      std::shared_ptr<TreeNode> temp_ptr = root;
      std::shared_ptr<TreeNode> previous_node = temp_ptr;
      while (temp_ptr) {
        previous_node = temp_ptr;
        if (comparator(data, temp_ptr->data)) {
          temp_ptr = temp_ptr->right;
        } else {
          temp_ptr = temp_ptr->left;
        }
      }
      if (comparator(previous_node->data, data)) {
        previous_node->left = new_node;
      } else {
        previous_node->right = new_node;
      }
    }
    size++;
  }
  void Dequeue() override {
    if (!root) {
      throw std::runtime_error("The queue is empty.");
    } else {
      std::shared_ptr<TreeNode> temp_ptr = root;
      std::shared_ptr<TreeNode> previous_node = nullptr;
      while (temp_ptr->right) {
        previous_node = temp_ptr;
        temp_ptr = temp_ptr->right;
      }
      if (previous_node) {
        previous_node->right = temp_ptr->left;
      } else {
        root = temp_ptr->left;
      }
      if (root) {
        previous_node = root;
        while (previous_node->right) {
          previous_node = previous_node->right;
        }
        the_highest_priority_node = previous_node;
      }
    }
    size--;
  }
  T Peek() override {
    if (the_highest_priority_node) {
      return the_highest_priority_node->data;
    } else {
      throw std::runtime_error("The queue is empty.");
    }
  }
  int GetSize() override {
    if (!root) {
      return 0;
    } else {
      return size;
    }
  }
  void Print() override {
    inOrderTraversal(root);
    std::cout << std::endl;
  }

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
  std::shared_ptr<TreeNode> the_highest_priority_node;
  int size;
  void inOrderTraversal(const std::shared_ptr<TreeNode>& node) const {
    if (node) {
      inOrderTraversal(node->left);
      std::cout << node->data << " \n";
      inOrderTraversal(node->right);
    }
  }
};

template <class T>
class Priority_queue_AVL_tree : public Priority_queue<T> {
 public:
  Priority_queue_AVL_tree(std::function<bool(const T&, const T&)> ncomparator)
      : comparator(ncomparator) {}
  void Enqueue(T data) override {
    root = Insert(root, data);
    the_highest_priority_node = FindTheHighestPriorityNode(root);
    size++;
  }
  void Dequeue() override {
    if (!root) {
      throw std::runtime_error("The queue is empty.");
    } else {
      root = DeleteTheHighestPriorityNode(root);
      the_highest_priority_node = FindTheHighestPriorityNode(root);
      size--;
    }
  }
  T Peek() override {
    if (the_highest_priority_node) {
      return the_highest_priority_node->data;
    } else {
      throw std::runtime_error("The queue is empty.");
    }
  }
  int GetSize() override {
    if (!root) {
      return 0;
    } else {
      return size;
    }
  }
  void Print() override {
    inOrderTraversal(root);
    std::cout << std::endl;
  }

 private:
  std::function<bool(const T&, const T&)> comparator;
  class TreeNode {
   public:
    TreeNode();
    TreeNode(T value) : data(value), height(1), left(nullptr), right(nullptr){};
    T data;
    std::shared_ptr<TreeNode> left;
    std::shared_ptr<TreeNode> right;
    int height;
  };
  std::shared_ptr<TreeNode> root;
  int size;
  int Height(std::shared_ptr<TreeNode> root) { return root ? root->height : 0; }
  int GetBalance(std::shared_ptr<TreeNode> root) {
    return root ? (Height(root->left) - Height(root->right)) : 0;
  }
  std::shared_ptr<TreeNode> RotateLeft(std::shared_ptr<TreeNode> root) {
    std::shared_ptr<TreeNode> right_child = root->right;
    std::shared_ptr<TreeNode> left_child_of_right_child = right_child->left;

    root->right = left_child_of_right_child;
    right_child->left = root;
    root->height = std::max(Height(root->left), Height(root->right)) + 1;
    right_child->height =
        std::max(Height(right_child->left), Height(right_child->right)) + 1;

    return right_child;
  }
  std::shared_ptr<TreeNode> RotateRight(std::shared_ptr<TreeNode> root) {
    std::shared_ptr<TreeNode> left_child = root->left;
    std::shared_ptr<TreeNode> right_child_of_left_child = left_child->right;

    root->left = right_child_of_left_child;
    left_child->right = root;
    root->height = std::max(Height(root->left), Height(root->right)) + 1;
    left_child->height =
        std::max(Height(left_child->left), Height(left_child->right)) + 1;

    return left_child;
  }
  std::shared_ptr<TreeNode> Insert(std::shared_ptr<TreeNode> root, T data) {
    if (!root) {
      return std::make_shared<TreeNode>(data);
    }
    if (comparator(data, root->data)) {
      root->right = Insert(root->right, data);
    } else {
      root->left = Insert(root->left, data);
    }
    root->height = std::max(Height(root->left), Height(root->right)) + 1;
    int balance = GetBalance(root);
    if (balance > 1) {
      if (comparator(data, root->left->data)) {
        root->left = RotateLeft(root->left);
        return RotateRight(root);
      } else {
        return RotateRight(root);
      }
    }
    if (balance < -1) {
      if (comparator(data, root->right->data)) {
        return RotateLeft(root);
      } else {
        root->right = RotateRight(root->right);
        return RotateLeft(root);
      }
    }
    return root;
  }
  std::shared_ptr<TreeNode> DeleteTheHighestPriorityNode(
      std::shared_ptr<TreeNode> root) {
    if (!root) {
      return root;
    }
    if (root->right) {
      root->right = DeleteTheHighestPriorityNode(root->right);
    } else {
      return root->left;
    }
    root->height = std::max(Height(root->left), Height(root->right)) + 1;
    int balance = GetBalance(root);
    if (balance > 1) {
      if (GetBalance(root->left) < 0) {
        root->left = RotateLeft(root->left);
        return RotateRight(root);
      } else {
        return RotateRight(root);
      }
    }
    if (balance < -1) {
      if (GetBalance(root->right) > 0) {
        root->right = RotateRight(root->right);
        return RotateLeft(root);
      } else {
        return RotateLeft(root);
      }
    }
    return root;
  }
  std::shared_ptr<TreeNode> FindTheHighestPriorityNode(
      std::shared_ptr<TreeNode> root) {
    if (root && root->right) {
      return FindTheHighestPriorityNode(root->right);
    }
    return root;
  }
  void inOrderTraversal(const std::shared_ptr<TreeNode>& node) const {
    if (node) {
      inOrderTraversal(node->left);
      std::cout << node->data << " \n";
      inOrderTraversal(node->right);
    }
  }
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