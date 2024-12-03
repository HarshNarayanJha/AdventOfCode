#include <cstddef>
#include <cstdio>
#include <fstream>
#include <iostream>

using namespace std;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

int part1() {
  string line;
  string instruction;
  ifstream input("../data/input3.txt", ios::in);

  if (input.is_open()) {

    while (getline(input, line)) {
      instruction.append(line);
    }

    input.close();
  }

  int result = 0;

  for (size_t i = 0; i < instruction.length(); i++) {
    bool match_mul = false;
    size_t j = i + 4;
    size_t comma = -1;

    // check if matches mul format
    if (instruction.at(i) == 'm' && instruction.substr(i + 1, 3) == "ul(") {
      // cout << "m and ul( matched at " << i << " and " << i + 1 << " to "
      // << i + 3 << endl;

      // cout << "checking for ending ), starting search from " << j << endl;

      while (j < instruction.length()) {
        if (instruction.at(j) != ',' && !isdigit(instruction.at(j)) &&
            instruction.at(j) != ')') {
          // cout << "found illegal char " << instruction.at(j)
          //      << ", breaking search." << endl;
          // cout << "since " << instruction.at(j)
          //      << " is not , or it is not digit " <<
          //      isdigit(instruction.at(j))
          //      << endl
          //      << endl;
          break;
        }

        if (instruction.at(j) == ',') {
          comma = j;
        }
        if (instruction.at(j) == ')') {
          match_mul = true;
          break;
        }
        j++;
      }
    }

    if (!match_mul)
      continue;

    size_t b_open = i + 3;
    size_t b_close = j;

    int n1, n2;

    n1 = stoi(instruction.substr(b_open + 1, comma - (b_open + 1)));
    n2 = stoi(instruction.substr(comma + 1, b_close - (comma + 1)));

    result += n1 * n2;
  }

  return result;
}

int part2() {
  string line;
  string instruction;
  ifstream input("../data/input3.txt", ios::in);

  if (input.is_open()) {

    while (getline(input, line)) {
      instruction.append(line);
    }

    input.close();
  }

  int result = 0;
  bool enabled = true;

  for (size_t i = 0; i < instruction.length(); i++) {
    bool match_mul = false;

    size_t j = i + 4;
    size_t comma = -1;

    // check if matches mul format
    if (instruction.at(i) == 'm' && instruction.substr(i + 1, 3) == "ul(") {

      while (j < instruction.length()) {
        if (instruction.at(j) != ',' && !isdigit(instruction.at(j)) &&
            instruction.at(j) != ')') {
          break;
        }

        if (instruction.at(j) == ',') {
          comma = j;
        }
        if (instruction.at(j) == ')') {
          match_mul = true;
          break;
        }
        j++;
      }
    } else if (instruction.at(i) == 'd' &&
               instruction.substr(i + 1, 3) == "o()") {
      enabled = true;
    } else if (instruction.at(i) == 'd' &&
               instruction.substr(i + 1, 6) == "on't()") {
      enabled = false;
    }

    if (!match_mul)
      continue;

    if (!enabled)
      continue;

    size_t b_open = i + 3;
    size_t b_close = j;

    int n1, n2;

    n1 = stoi(instruction.substr(b_open + 1, comma - (b_open + 1)));
    n2 = stoi(instruction.substr(comma + 1, b_close - (comma + 1)));

    result += n1 * n2;
  }

  return result;
}
