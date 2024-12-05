#include <algorithm>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

using namespace std;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

void parse_input(ifstream &input, map<int, vector<int>> &rules,
                 vector<vector<int>> &orders) {
  string line;
  bool rules_done = false;
  while (getline(input, line)) {
    if (line.empty()) {
      rules_done = true;
      continue;
    }

    if (!rules_done) {
      rules[stoi(line.substr(0, line.find('|')))].push_back(
          stoi(line.substr(line.find('|') + 1, line.size())));
    } else {
      stringstream ss(line);
      string c;
      vector<int> order;
      while (getline(ss, c, ',')) {
        order.push_back(stoi(c));
      }

      orders.push_back(order);
    }
  }
}

int part1() {
  string line;
  ifstream input("../data/input5.txt");

  map<int, vector<int>> rules;
  vector<vector<int>> orders;

  if (input.is_open()) {
    parse_input(input, rules, orders);
    input.close();
  }

  vector<int> valids;

  for (size_t o = 0; o < orders.size(); o++) {
    bool is_valid = true;

    for (size_t i = 0; i < orders[o].size(); i++) {
      int page = orders[o][i];

      if (rules.count(page) == 0) {
        continue;
      }

      for (size_t k = 0; k < i; k++) {
        if (count(rules[page].begin(), rules[page].end(), orders[o][k]) > 0) {
          is_valid = false;
          break;
        }
      }

      if (!is_valid)
        break;
    }

    if (is_valid) {
      valids.push_back(o);
    }
  }

  int middle_sum = 0;
  for (size_t i = 0; i < valids.size(); i++) {
    middle_sum += orders[valids[i]][orders[valids[i]].size() / 2];
  }

  return middle_sum;
}

int part2() {
  string line;
  ifstream input("../data/input5.txt");

  map<int, vector<int>> rules;
  vector<vector<int>> orders;

  if (input.is_open()) {
    parse_input(input, rules, orders);
    input.close();
  }

  vector<int> invalids;

  for (size_t o = 0; o < orders.size(); o++) {
    bool is_valid = true;

    for (size_t i = 0; i < orders[o].size(); i++) {
      int page = orders[o][i];

      if (rules.count(page) == 0) {
        continue;
      }

      for (size_t k = 0; k < i; k++) {
        if (count(rules[page].begin(), rules[page].end(), orders[o][k]) > 0) {
          is_valid = false;
          break;
        }
      }

      if (!is_valid)
        break;
    }

    if (!is_valid) {
      invalids.push_back(o);
    }
  }

  // "fix" invalids

  for (size_t o = 0; o < invalids.size(); o++) {
    vector<int> &order = orders[invalids[o]];
    for (size_t i = 0; i < order.size(); i++) {
      for (size_t j = 1; j < order.size(); j++) {
        if (rules.count(order[j]) == 0)
          continue;
        if (count(rules[order[j]].begin(), rules[order[j]].end(),
                  order[j - 1]) > 0) {
          // swap!
          int temp = order[j];
          order[j] = order[j - 1];
          order[j - 1] = temp;
        }
      }
    }
  }

  int middle_sum = 0;
  for (size_t i = 0; i < invalids.size(); i++) {
    auto order = orders[invalids[i]];
    middle_sum += order[order.size() / 2];
  }

  return middle_sum;
}
