#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
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
  ifstream input("../data/input12.txt");

  vector<vector<char>> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      vector<char> i(line.begin(), line.end());
      grid.push_back(i);
    }
    input.close();
  }

  int H = grid.size();
  int W = grid[0].size();

  map<int, vector<Point>> regions;
  set<Point> visited;
  int component_id = 0;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (visited.count({i, j}) != 0) {
        continue;
      }

      vector<Point> component;

      // dfs
      vector<Point> stack;
      stack.push_back({i, j});

      while (!stack.empty()) {
        Point c = stack.back();
        int ci = c.first, cj = c.second;

        stack.pop_back();

        if (visited.count(c) != 0) {
          continue;
        }

        visited.insert(c);
        component.push_back(c);

        set<Point> neighbours = {
            {ci - 1, cj}, {ci + 1, cj}, {ci, cj - 1}, {ci, cj + 1}};
        for (const auto &n : neighbours) {
          int ni = n.first, nj = n.second;
          if (ni >= 0 && ni < H && nj >= 0 && nj < W) {
            if (grid[ni][nj] == grid[i][j] && visited.count(n) == 0) {
              stack.push_back(n);
            }
          }
        }
      }
      // dfs end

      regions[component_id] = component;
      component_id += 1;
    }
  }

  int cost = 0;

  for (const auto &r : regions) {
    vector<Point> span = r.second;
    int area = span.size();
    int perimeter = 0;

    for (const auto &p : span) {
      int i = p.first, j = p.second;

      set<Point> neighbours = {{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}};
      for (const auto n : neighbours) {
        if (count(span.begin(), span.end(), n) == 0) {
          perimeter++;
        }
      }
    }
    cost += area * perimeter;
  }

  return cost;
}

int part2() {
  string line;
  ifstream input("../data/input12.txt");

  vector<vector<char>> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      vector<char> i(line.begin(), line.end());
      grid.push_back(i);
    }
    input.close();
  }

  int H = grid.size();
  int W = grid[0].size();

  map<int, vector<Point>> regions;
  set<Point> visited;
  int component_id = 0;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (visited.count({i, j}) != 0) {
        continue;
      }

      vector<Point> component;

      // dfs
      vector<Point> stack;
      stack.push_back({i, j});

      while (!stack.empty()) {
        Point c = stack.back();
        int ci = c.first, cj = c.second;

        stack.pop_back();

        if (visited.count(c) != 0) {
          continue;
        }

        visited.insert(c);
        component.push_back(c);

        set<Point> neighbours = {
            {ci - 1, cj}, {ci + 1, cj}, {ci, cj - 1}, {ci, cj + 1}};
        for (const auto &n : neighbours) {
          int ni = n.first, nj = n.second;
          if (ni >= 0 && ni < H && nj >= 0 && nj < W) {
            if (grid[ni][nj] == grid[i][j] && visited.count(n) == 0) {
              stack.push_back(n);
            }
          }
        }
      }
      // dfs end

      regions[component_id] = component;
      component_id += 1;
    }
  }

  int cost = 0;

  for (const auto &r : regions) {
    vector<Point> span = r.second;
    int area = span.size();
    vector<pair<Point, Point>> perimeter;

    for (const auto &p : span) {
      int i = p.first, j = p.second;

      set<Point> neighbours = {{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}};
      for (const auto n : neighbours) {
        if (count(span.begin(), span.end(), n) == 0) {
          perimeter.push_back({p, n});
        }
      }
    }

    vector<pair<Point, Point>> sides;

    for (const auto &p : perimeter) {
      Point i = p.first, j = p.second;
      bool remove = false;

      set<Point> check = {{1, 0}, {0, 1}};

      for (const auto &c : check) {
        Point ni = {i.first + c.first, i.second + c.second};
        Point nj = {j.first + c.first, j.second + c.second};

        pair<Point, Point> edge = {ni, nj};
        if (count(perimeter.begin(), perimeter.end(), edge) != 0) {
          remove = true;
        }
      }

      if (!remove) {
        sides.push_back({i, j});
      }
    }
    cost += area * sides.size();
  }

  return cost;
}
