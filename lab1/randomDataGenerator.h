#ifndef RANDOM_DATA_GENERATOR_H
#define RANDOM_DATA_GENERATOR_H

#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>

#include "book.h"

namespace myrandomdatagenerator {
class Random_data_generator {
 public:
  static int GetRandomIntData() {
    std::random_device rd;
    int randInt;
    std::uniform_int_distribution<int> distribution(-1000, 1000);
    std::default_random_engine engine(rd());
    randInt = distribution(engine);
    return randInt;
  }
  static double GetRandomDoubleData() {
    std::random_device rd;
    double randDouble;
    std::uniform_real_distribution<double> distribution(-1000.0, 1000.0);
    std::default_random_engine engine(rd());
    randDouble = distribution(engine);
    return randDouble;
  }
  static char GetRandomCharData() {
    char randChar = 'a' + std::rand() % 26;
    return randChar;
  }
  static std::string GetRandomStringData() {
    const char charSet[] =
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
  template <typename T>
  static std::vector<T> GetRandomVectorData() {
    int numOfElements = rand() % 20 + 1;
    std::vector<T> randVector;
    if constexpr (std::is_same_v<T, int>) {
      for (int i = 1; i <= numOfElements; i++) {
        randVector.push_back(
            myrandomdatagenerator::Random_data_generator::GetRandomIntData());
      }
    } else if constexpr (std::is_same_v<T, double>) {
      for (int i = 0; i < numOfElements; i++) {
        randVector.push_back(myrandomdatagenerator::Random_data_generator::
                                 GetRandomDoubleData());
      }
    } else if constexpr (std::is_same_v<T, char>) {
      for (int i = 0; i < numOfElements; i++) {
        randVector.push_back(
            myrandomdatagenerator::Random_data_generator::GetRandomCharData());
      }
    } else if constexpr (std::is_same_v<T, std::string>) {
      for (int i = 0; i < numOfElements; i++) {
        randVector.push_back(myrandomdatagenerator::Random_data_generator::
                                 GetRandomStringData());
      }
    }
    return randVector;
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
    int randNumOfAliases = std::rand() % 5 + 1;
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
    for (int i = 0; i < randNumOfAliases; i++) {
      int aliasNum = std::rand() % aliasesNum;
      randCharacter.AddAlias(aliases[aliasNum]);
    }
    int numOfBooks = std::rand() % 7 + 3;
    for (int i = 0; i < numOfBooks; i++) {
      randCharacter.AddBookAndRole(GetRandomBookData(), generateRandomRole());
    }
    return randCharacter;
  }
  static mybook::Series GetRandomSeriesData() {
    mybook::Series randSeries;
    mybook::Character randCharacter = GetRandomCharacterData();
    randSeries = randCharacter.CreateSeries();
    return randSeries;
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