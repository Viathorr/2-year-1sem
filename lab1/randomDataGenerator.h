#ifndef RANDOM_DATA_GENERATOR_H
#define RANDOM_DATA_GENERATOR_H

#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "book.h"

namespace myrandomdatagenerator {
class Random_data_generator {
 public:
  static int GetRandomIntData() { return std::rand() % 1000 + 1; }
  static double GetRandomDoubleData() { return std::rand() % 1000 + 1.001; }
  static char GetRandomCharData() {
    char randChar = 'a' + std::rand() % 26;
    return randChar;
  }
  static std::string GetRandomStringData() {
    const char charSet[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    std::string randString;
    int length = rand() % 30 + 2;
    randString.reserve(length);

    for (int i = 0; i < length; i++) {
      randString += charSet[rand() % (sizeof(charSet) - 1)];
    }
    return randString;
  }
  static mybook::Book GetRandomBookData() {
    mybook::Book randBook;
    int booksNum = 32;
    std::ifstream file("books.txt");
    if (!file.is_open()) {
      std::cerr << "File is not opened!";
    }
    std::vector<std::string> books;
    std::string line;
    while (!file.eof()) {
      std::getline(file, line);
      books.push_back(line);
    }
    file.close();
    int randBookNum = rand() % 32;
    std::stringstream stream;
    stream << books[randBookNum];
    std::string title, author, annotation;
    std::getline(stream, title, ',');
    std::getline(stream, author, ',');
    std::getline(stream, annotation);
    int year, numOfPages;
    year = std::rand() % 224 + 1800;
    numOfPages = std::rand() % 800 + 101;
    randBook.SetTitle(title);
    randBook.SetAuthor(author);
    randBook.SetAnnotation(annotation);
    randBook.SetYear(year);
    randBook.SetAmountOfPages(numOfPages);

    return randBook;
  }
  static mybook::Character GetRandomCharacterData() {
    mybook::Character randCharacter;
    int aliasesNum = 45;
    int aliasNum = std::rand() % 45;
    std::ifstream file("aliases.txt");
    if (!file.is_open()) {
      std::cerr << "File is not opened!";
    }
    std::vector<std::string> aliases;
    std::string alias;
    while (!file.eof()) {
      std::getline(file, alias);
      aliases.push_back(alias);
    }
    file.close();
    randCharacter.AddAlias(aliases[aliasNum]);
    int numOfBooks = std::rand() % 10 + 1;
    for (int i = 0; i < numOfBooks; i++) {
      randCharacter.AddBookAndRole(GetRandomBookData(), generateRandomRole());
    }
    return randCharacter;
  }

 private:
  static mybook::Role generateRandomRole() {
    int randomValue = rand() % 3;
    switch (randomValue) {
      case 0:
        return mybook::Role::kMain;
      case 1:
        return mybook::Role::kSupporting;
      case 2:
        return mybook::Role::kMinor;
    }
    return mybook::Role::kMain;
  }
};
}  // namespace myrandomdatagenerator
#endif