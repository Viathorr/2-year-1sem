#ifndef BOOK_H
#define BOOK_H

#include <iostream>
#include <vector>

namespace mybook {
enum Role { kMain, kSupporting, kMinor };
std::string RoleToString(Role role);

class Book {
 public:
  Book(){};  // default ctor
  Book(std::string title, std::string author, int year, int amount,
       std::string annotation);
  void SetTitle(std::string title);
  void SetAuthor(std::string author);
  void SetYear(int year);
  void SetAmountOfPages(int amount);
  void SetAnnotation(std::string annotation);
  std::string GetTitle() const;
  std::string GetAuthor() const;
  int GetYear() const;
  int GetAmountOfPages() const;
  std::string GetAnnotation() const;
  friend std::ostream& operator<<(std::ostream& os, const Book& book);

 private:
  std::string title;
  std::string author;
  int year;
  int amountOfPages;
  std::string annotation;
};

class Series {
 public:
  void AddBook(Book title);  // add book in sorted order by year
  const std::vector<Book>& GetListOfBooks() const;
  int AmountOfBooks() const;
  friend std::ostream& operator<<(std::ostream& os, const Series& series);

 private:
  std::vector<Book> listOfBooks;
};

class Character {
 public:
  void AddAlias(std::string name);
  void AddBookAndRole(Book book, Role role);
  int AmountOfBooksWhereCharacterIsPresent() const;
  const std::vector<std::string>& GetAliases() const;
  const std::vector<std::pair<Book, Role>>&
  GetSetOfBooksWhereCharacterIsPresent() const;
  Series CreateSeries();  // create series from books where character is main
                          // or supporting
  friend std::ostream& operator<<(std::ostream& os, const Character& character);

 private:
  std::vector<std::string> aliases;
  std::vector<std::pair<Book, Role>> appearsIn;
};
}  // namespace mybook

#endif