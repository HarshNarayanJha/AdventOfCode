#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <set>
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
  ifstream input("../data/input4.txt");

  vector<vector<char>> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      vector<char> row(line.begin(), line.end());
      grid.push_back(row);
    }
    input.close();
  }

  const int N = grid.size();

  int count = 0;

  set<pair<int, int>> directions;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i == 0 and j == 0)
        continue;
      directions.insert({i, j});
    }
  }

  for (int x = 0; x < N; x++) {
    for (int y = 0; y < N; y++) {

      for (auto d : directions) {
        if ((x + d.first * 3 < 0 || x + d.first * 3 >= N) ||
            (y + d.second * 3 < 0 || y + d.second * 3 >= N))
          continue;

        string word;

        for (int n = 0; n < 4; n++) {
          word.push_back(grid[x + d.first * n][y + d.second * n]);
        }

        if (word == "XMAS") {
          count++;
        }
      }
    }
  }

  return count;
}

int part2() {
  string line;
  ifstream input("../data/input4.txt");

  vector<vector<char>> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      vector<char> row(line.begin(), line.end());
      grid.push_back(row);
    }
    input.close();
  }

  const int N = grid.size();

  int count = 0;

  for (int x = 0; x < N; x++) {
    for (int y = 0; y < N; y++) {

      if ((x + 2 < 0 || x + 2 >= N) || (y + 2 < 0 || y + 2 >= N))
        continue;

      if (grid[x + 1][y + 1] != 'A')
        continue;

      string word1;
      string word2;

      for (int n = 0; n < 3; n++) {
        word1.push_back(grid[x + n][y + n]);
        word2.push_back(grid[x + n][y + 2 - n]);
      }

      if ((word1 == "MAS" || word1 == "SAM") &&
          (word2 == "MAS" || word2 == "SAM")) {
        count++;
      }
    }
  }

  return count;
}
