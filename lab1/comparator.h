#ifndef COMPARATOR_H
#define COMPARATOR_H

#include <string>
#include <vector>

#include "book.h"

namespace mycomparator {
bool comparatorInt(const int& a, const int& b) { return a > b; }
bool comparatorDouble(const double& a, const double& b) { return a > b; }
bool comparatorChar(const char& a, const char& b) { return a > b; }
bool comparatorString(const std::string& a, const std::string& b) {
  return a.length() > b.length();
}
template <typename T>
bool comparatorVector(const std::vector<T>& a, const std::vector<T>& b) {
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
}  // namespace mycomparator
#endif