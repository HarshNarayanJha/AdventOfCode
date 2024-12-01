#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int day1();
int day2();

int main() {
  cout << day1() << endl;
  cout << day2() << endl;
}

int day1() {
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

int day2() { return 1; }
