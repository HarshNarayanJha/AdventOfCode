#include <fstream>
#include <iostream>
#include <set>
#include <vector>

using namespace std;
using Point = pair<int, int>;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

int part1() {
  string line;
  ifstream input("../data/input10.txt");

  vector<vector<char>> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      grid.emplace_back(line.begin(), line.end());
    }
    input.close();
  }

  int H = grid.size();
  int W = grid[0].size();

  set<Point> trailheads;
  set<Point> tops;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (grid[i][j] == '0') {
        trailheads.insert({i, j});
      } else if (grid[i][j] == '9') {
        tops.insert({i, j});
      }
    }
  }

  int scores = 0;

  set<Point> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  for (auto trailhead : trailheads) {
    set<Point> visited;
    vector<Point> stack = {trailhead};

    while (!stack.empty()) {
      Point pt = stack.back();
      stack.pop_back();

      if ((tops.count(pt) != 0) and (visited.count(pt) == 0)) {
        scores++;
        visited.insert(pt);
      }

      for (auto d : directions) {
        int new_x = d.first + pt.first, new_y = d.second + pt.second;

        if (new_x >= 0 && new_x < H && new_y >= 0 && new_y < W &&
            grid[new_x][new_y] == grid[pt.first][pt.second] + 1) {
          stack.push_back({new_x, new_y});
        }
      }
    }
  }

  return scores;
}

int part2() {
  string line;
  ifstream input("../data/input10.txt");

  vector<vector<char>> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      grid.emplace_back(line.begin(), line.end());
    }
    input.close();
  }

  int H = grid.size();
  int W = grid[0].size();

  set<Point> trailheads;
  set<Point> tops;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (grid[i][j] == '0') {
        trailheads.insert({i, j});
      } else if (grid[i][j] == '9') {
        tops.insert({i, j});
      }
    }
  }

  int ratings = 0;

  set<Point> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  for (auto trailhead : trailheads) {
    vector<Point> stack = {trailhead};

    while (!stack.empty()) {
      Point pt = stack.back();
      stack.pop_back();

      if ((tops.count(pt) != 0)) {
        ratings++;
      }

      for (auto d : directions) {
        int new_x = d.first + pt.first, new_y = d.second + pt.second;

        if (new_x >= 0 && new_x < H && new_y >= 0 && new_y < W &&
            grid[new_x][new_y] == grid[pt.first][pt.second] + 1) {
          stack.push_back({new_x, new_y});
        }
      }
    }
  }

  return ratings;
}
