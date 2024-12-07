#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

long int part1();
long int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

long int part1() {
  string line;
  ifstream input("../data/input7.txt");

  map<long int, vector<int>> equations;

  if (input.is_open()) {
    while (getline(input, line)) {
      stringstream ss(line.substr(line.find(':') + 2));
      long int result = stol(line.substr(0, line.find(':')));

      vector<int> values;

      string val;
      while (ss >> val) {
        values.push_back(stol(val));
      }

      equations[result] = values;
    }
    input.close();
  }

  set<char> operators = {'+', '*'};
  long int true_sum = 0;

  for (auto keyval : equations) {
    long int result = keyval.first;
    vector<int> values = keyval.second;
    int count = values.size() - 1;
    bool found = false;

    vector<vector<char>> ops_combs;
    for (int i = 0; i < pow(operators.size(), count); i++) {
      vector<char> ops;
      int num = i;
      for (int j = 0; j < count; j++) {
        auto it = operators.begin();
        advance(it, num % operators.size());
        ops.push_back(*it);
        num /= operators.size();
      }
      ops_combs.push_back(ops);
    }

    for (auto op_comb : ops_combs) {
      long int curr = values[0];

      for (size_t i = 0; i < op_comb.size(); i++) {
        if (op_comb[i] == '+') {
          curr += values[i + 1];
        } else if (op_comb[i] == '*') {
          curr *= values[i + 1];
        }
      }

      if (curr == result) {
        found = true;
        break;
      }
    }

    if (found) {
      true_sum += result;
    }
  }

  return true_sum;
}

long int part2() {
  string line;
  ifstream input("../data/input7.txt");

  map<long int, vector<int>> equations;

  if (input.is_open()) {
    while (getline(input, line)) {
      stringstream ss(line.substr(line.find(':') + 2));
      long int result = stol(line.substr(0, line.find(':')));

      vector<int> values;

      string val;
      while (ss >> val) {
        values.push_back(stol(val));
      }

      equations[result] = values;
    }
    input.close();
  }

  set<char> operators = {'+', '*', '|'};
  long int true_sum = 0;

  for (auto keyval : equations) {
    long int result = keyval.first;
    vector<int> values = keyval.second;
    int count = values.size() - 1;
    bool found = false;

    vector<vector<char>> ops_combs;
    for (int i = 0; i < pow(operators.size(), count); i++) {
      vector<char> ops;
      int num = i;
      for (int j = 0; j < count; j++) {
        auto it = operators.begin();
        advance(it, num % operators.size());
        ops.push_back(*it);
        num /= operators.size();
      }
      ops_combs.push_back(ops);
    }

    for (auto op_comb : ops_combs) {
      long int curr = values[0];

      for (size_t i = 0; i < op_comb.size(); i++) {
        if (op_comb[i] == '+') {
          curr += values[i + 1];
        } else if (op_comb[i] == '*') {
          curr *= values[i + 1];
        } else if (op_comb[i] == '|') {
          curr = curr * (int)pow(10, (int)(log10(values[i + 1]) + 1)) +
                 values[i + 1];
        }
      }

      if (curr == result) {
        found = true;
        break;
      }
    }

    if (found) {
      true_sum += result;
    }
  }

  return true_sum;
}
