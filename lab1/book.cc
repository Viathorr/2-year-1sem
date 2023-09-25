#include "book.h"

namespace mybook {
std::string RoleToString(Role role) {
  switch (role) {
    case Role::kMain:
      return "main";
    case Role::kSupporting:
      return "supporting";
    case Role::kMinor:
      return "minor";
    default:
      return "Unknown";
  }
}
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

std::ostream& operator<<(std::ostream& os, const Book& book) {
  os << "\nBOOK:\n";
  os << "Title: \"" << book.GetTitle() << "\", author: " << book.GetAuthor()
     << ", year: " << book.GetYear() << ", " << book.GetAmountOfPages()
     << " pages, annotation: \"" << book.GetAnnotation() << "\".\n";
  return os;
}
void Character::AddAlias(std::string name) { aliases.push_back(name); }
void Character::AddBookAndRole(Book book, Role role) {
  appearsIn.push_back({book, role});
}
int Character::AmountOfBooksWhereCharacterIsPresent() const {
  return appearsIn.size();
}
const std::vector<std::string>& Character::GetAliases() const {
  return aliases;
}
const std::vector<std::pair<Book, Role>>&
Character::GetSetOfBooksWhereCharacterIsPresent() const {
  return appearsIn;
}
std::ostream& operator<<(std::ostream& os, const Series& series) {
  os << "\nSERIES:\n"
     << "Books: ";
  for (const Book& book : series.listOfBooks) {
    os << "\"" << book.GetTitle() << "\" \n";
  }
  return os;
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
const std::vector<Book>& Series::GetListOfBooks() const { return listOfBooks; }
Series Character::CreateSeries() {
  Series series;
  for (const auto& pair : appearsIn) {
    if (pair.second == Role::kMain || pair.second == Role::kSupporting)
      series.AddBook(pair.first);
  }
  return series;
}
std::ostream& operator<<(std::ostream& os, const Character& character) {
  os << "\nCHARACTER:\n"
     << "Character aliases: ";
  for (const std::string& alias : character.aliases) {
    os << alias << ", ";
  }
  os << "appears in such books:\n";
  for (const auto& bookRolePair : character.appearsIn) {
    os << "book title: \"" << bookRolePair.first.GetTitle()
       << "\", role: " << RoleToString(bookRolePair.second) << "\n";
  }
  return os;
}
}  // namespace mybook