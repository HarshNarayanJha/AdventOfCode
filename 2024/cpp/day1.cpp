#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

int part1() {
  string line;
  ifstream input;
  input.open("../input1.txt", ios::in);

  vector<int> list1;
  vector<int> list2;

  if (input.is_open()) {
    while (getline(input, line)) {
      stringstream ss(line);

      string s;
      int i = 0;
      while (ss >> s) {
        if (i == 0) {
          list1.push_back(stoi(s));
          i = 1;
        } else {
          list2.push_back(stoi(s));
          i = 0;
        }
      }
    }
    input.close();
  }

  sort(list1.begin(), list1.end());
  sort(list2.begin(), list2.end());

  size_t i = 0;

  int dist_sum = 0;

  while (i < list1.size()) {
    dist_sum += abs(list1.at(i) - list2.at(i));
    i++;
  }

  return dist_sum;
}

int part2() {
  string line;
  ifstream input;
  input.open("../input1.txt", ios::in);

  vector<int> list1;
  unordered_map<int, int> map2;

  if (input.is_open()) {
    while (getline(input, line)) {
      stringstream ss(line);

      string s;
      int i = 0;
      while (ss >> s) {
        if (i == 0) {
          list1.push_back(stoi(s));
          i = 1;
        } else {
          int value = stoi(s);
          if (map2.count(value)) {
            map2[value]++;
          } else {
            map2[value] = 1;
          }
          i = 0;
        }
      }
    }
    input.close();
  }

  size_t i = 0;

  int sim_score = 0;

  while (i < list1.size()) {
    int value = list1.at(i);
    if (map2.count(value)) {
      sim_score += value * map2[value];
    }
    i++;
  }

  return sim_score;
}
