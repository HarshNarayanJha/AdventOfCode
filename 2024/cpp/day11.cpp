#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <sys/types.h>
#include <vector>

using namespace std;

long int part1();
long int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

long int part1() {
  string l;
  ifstream input("../data/input11.txt");
  vector<int> line;

  if (input.is_open()) {
    getline(input, l);
    stringstream ss(l);
    string each;
    while (ss >> each) {
      line.push_back(stoi(each));
    }
    input.close();
  }

  int blinks = 25;
  map<long int, long int> counts;

  for (auto d : line) {
    counts[d]++;
  }

  for (int i = 0; i < blinks; i++) {
    map<long int, long int> new_counts;
    new_counts[1] = counts[0];

    for (const auto entry : counts) {
      long int num = entry.first, count = entry.second;

      if (num != 0) {
        string s = to_string(num);

        if (s.size() % 2 == 1) {
          long int new_key = 2024 * num;
          new_counts[new_key] = new_counts[new_key] + count;

        } else {
          long int mid = s.size() / 2;
          long int left = stoi(s.substr(0, mid)), right = stoi(s.substr(mid));
          new_counts[left] = new_counts[left] + count;
          new_counts[right] = new_counts[right] + count;
        }
      }
    }

    counts = new_counts;
  }

  long int sum = 0;
  for (auto keyval : counts) {
    sum += keyval.second;
  }

  return sum;
}

long int part2() {
  string l;
  ifstream input("../data/input11.txt");
  vector<int> line;

  if (input.is_open()) {
    getline(input, l);
    stringstream ss(l);
    string each;
    while (ss >> each) {
      line.push_back(stoi(each));
    }
    input.close();
  }

  int blinks = 75;
  map<long int, long int> counts;

  for (auto d : line) {
    counts[d]++;
  }

  for (int i = 0; i < blinks; i++) {
    map<long int, long int> new_counts;
    new_counts[1] = counts[0];

    for (const auto entry : counts) {
      long int num = entry.first, count = entry.second;

      if (num != 0) {
        string s = to_string(num);

        if (s.size() % 2 == 1) {
          long int new_key = 2024 * num;
          new_counts[new_key] = new_counts[new_key] + count;

        } else {
          long int mid = s.size() / 2;
          long int left = stoi(s.substr(0, mid)), right = stoi(s.substr(mid));
          new_counts[left] = new_counts[left] + count;
          new_counts[right] = new_counts[right] + count;
        }
      }
    }

    counts = new_counts;
  }

  long int sum = 0;
  for (auto keyval : counts) {
    sum += keyval.second;
  }

  return sum;
}
