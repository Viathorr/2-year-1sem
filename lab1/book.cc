#include "book.h"

namespace mybook {
Book::Book(std::string title, std::string author, int year, int amount,
           std::string annotation) {
  this->title = title;
  this->author = author;
  this->year = year;
  amountOfPages = amount;
  this->annotation = annotation;
}
void Book::SetTitle(std::string title) { this->title = title; }
void Book::SetAuthor(std::string author) { this->author = author; }
void Book::SetYear(int year) { this->year = year; }
void Book::SetAmountOfPages(int amount) { amountOfPages = amount; }
void Book::SetAnnotation(std::string annotation) {
  this->annotation = annotation;
}
std::string Book::GetTitle() const { return title; }
std::string Book::GetAuthor() const { return author; }
int Book::GetYear() const { return year; }
int Book::GetAmountOfPages() const { return amountOfPages; }
std::string Book::GetAnnotation() const { return annotation; }

void Character::AddAlias(std::string name) { aliases.push_back(name); }
void Character::AddBookAndRole(Book book, Role role) {
  appearsIn.push_back({book, role});
}
int Character::AmountOfBooksWhereCharacterIsPresent() const {
  return appearsIn.size();
}
const std::vector<std::string> &Character::GetAliases() const {
  return aliases;
}
const std::vector<std::pair<Book, Role>> &
Character::GetSetOfBooksWhereCharacterIsPresent() const {
  return appearsIn;
}
void Series::AddBook(Book title) {
  if (!listOfBooks.size())
    listOfBooks.push_back(title);
  else {
    for (int i = 0; i < listOfBooks.size(); i++) {
      if (title.GetYear() < listOfBooks[i].GetYear()) {
        listOfBooks.insert(listOfBooks.begin() + i, title);
        break;
      }
    }
  }
}
int Series::AmountOfBooks() const { return listOfBooks.size(); }
const std::vector<Book> &Series::GetListOfBooks() const { return listOfBooks; }
Series Character::CreateSeries() {
  Series series;
  for (const auto &pair : appearsIn) {
    if (pair.second == Role::kMain || pair.second == Role::kSupporting)
      series.AddBook(pair.first);
  }
  return series;
}

}  // namespace mybook