#include <algorithm>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <utility>
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
  ifstream input("../data/input9.txt");

  if (input.is_open()) {
    getline(input, line);
    input.close();
  }

  vector<int> fs;
  int fid = 0;
  int i = 0;
  for (char b : line) {
    int t = b - '0';
    if (i == 0) {
      for (int i = 0; i < t; i++) {
        fs.push_back(fid);
      }

      fid++;
    } else if (i == 1) {
      for (int i = 0; i < t; i++) {
        fs.push_back(-1);
      }
    }

    i = (i + 1) % 2;
  }

  int N = fs.size();
  int count_files = N - count(fs.begin(), fs.end(), -1);

  long int checksum = 0;
  int last_checked = N;

  for (int b = 0; b < N; b++) {
    if (b == count_files) {
      break;
    }
    if (fs[b] == -1) {
      int idx = last_checked - 1;
      while (fs[idx] == -1) {
        idx -= 1;
      }

      checksum += b * fs[idx];

      last_checked = idx;
    } else {
      checksum += b * fs[b];
    }
  }

  return checksum;
}

long int part2() {
  string line;
  ifstream input("../data/input9.txt");

  if (input.is_open()) {
    getline(input, line);
    input.close();
  }

  vector<int> fs;
  int fid = 0;
  int i = 0;
  for (char b : line) {
    int t = b - '0';
    if (i == 0) {
      for (int i = 0; i < t; i++) {
        fs.push_back(fid);
      }

      fid++;
    } else if (i == 1) {
      for (int i = 0; i < t; i++) {
        fs.push_back(-1);
      }
    }

    i = (i + 1) % 2;
  }

  int N = fs.size();

  int b = N - 1;

  while (b >= 0) {
    if (fs[b] != -1) {
      int file_from = b;
      int file_to = file_from;
      int fid = fs[file_from];
      while (fs[file_to] == fid) {
        file_to -= 1;
      }
      int fsize = file_from - file_to;

      // find empty space
      int empty_from = 0;
      int esize = 0;
      while (empty_from < b) {
        while (empty_from < b and fs[empty_from] != -1) {
          empty_from += 1;
        }
        while (empty_from + esize < b and fs[empty_from + esize] == -1) {
          esize += 1;
        }
        if (esize >= fsize) {
          break;
        }
        empty_from += 1;
        esize = 0;
      }

      if (fsize <= esize) {
        for (int i = 0; i < fsize; i++) {
          swap(fs[empty_from + i], fs[file_from - i]);
        }
      }

      b = b - fsize;
    } else {
      b -= 1;
    }
  }

  long int checksum = 0;
  for (int i = 0; i < N; i++) {
    if (fs[i] == -1)
      continue;
    checksum += i * fs[i];
  }

  return checksum;
}
