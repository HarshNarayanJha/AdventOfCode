#include <cstdio>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <sys/types.h>
#include <unordered_map>
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
  unordered_map<long int, long int> counts;

  for (const auto &d : line) {
    counts[d]++;
  }

  for (int i = 0; i < blinks; i++) {
    unordered_map<long int, long int> new_counts;
    new_counts.reserve(counts.size() * 2);
    new_counts[1] = counts[0];

    for (const auto &entry : counts) {
      long int num = entry.first, count = entry.second;

      if (num != 0) {
        string s = to_string(num);
        const size_t size = s.size();

        if (size % 2 == 1) {
          new_counts[2024 * num] += count;
        } else {
          const size_t mid = size / 2;
          new_counts[stol(s.substr(0, mid))] += count;
          new_counts[stol(s.substr(mid))] += count;
        }
      }
    }

    counts = std::move(new_counts);
  }

  long int sum = 0;
  for (const auto &keyval : counts) {
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
  unordered_map<long int, long int> counts;

  for (const auto &d : line) {
    counts[d]++;
  }

  for (int i = 0; i < blinks; i++) {
    unordered_map<long int, long int> new_counts;
    new_counts.reserve(counts.size() * 2);
    new_counts[1] = counts[0];

    for (const auto &entry : counts) {
      long int num = entry.first, count = entry.second;

      if (num != 0) {
        string s = to_string(num);
        const size_t size = s.size();

        if (size % 2 == 1) {
          new_counts[2024 * num] += count;
        } else {
          const size_t mid = size / 2;
          new_counts[stol(s.substr(0, mid))] += count;
          new_counts[stol(s.substr(mid))] += count;
        }
      }
    }

    counts = std::move(new_counts);
  }

  long int sum = 0;
  for (const auto &keyval : counts) {
    sum += keyval.second;
  }

  return sum;
}
