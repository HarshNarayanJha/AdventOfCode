#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

using Point = pair<int, int>;

auto get_two_antinodes(Point p1, Point p2) {
  int x1 = p1.first, y1 = p1.second;
  int x2 = p2.first, y2 = p2.second;
  int dx = x2 - x1;
  int dy = y2 - y1;
  Point a1 = {x1 - dx, y1 - dy};
  Point a2 = {x2 + dx, y2 + dy};

  return pair<Point, Point>(a1, a2);
}

bool node_in_bound(Point p, int w, int h) {
  return p.first >= 0 && p.first < h && p.second >= 0 && p.second < w;
}

int part1() {
  string line;
  ifstream input("../data/input8.txt");

  vector<string> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      grid.push_back(line);
    }
    input.close();
  }

  int H = grid.size();
  int W = grid[0].size();

  map<char, vector<Point>> antennas;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (grid[i][j] == '.')
        continue;
      antennas[grid[i][j]].push_back({i, j});
    }
  }

  set<Point> antinodes_at;

  for (auto keyval : antennas) {
    vector<Point> points = keyval.second;

    vector<pair<Point, Point>> pairs;

    for (size_t i = 0; i < points.size(); i++) {
      for (size_t j = 0; j < points.size(); j++) {
        if (i == j)
          continue;

        pairs.push_back({points[i], points[j]});
      }
    }

    set<pair<Point, Point>> visited_pairs;

    for (auto p : pairs) {
      Point a = p.first;
      Point b = p.second;

      pair<Point, Point> pair1 = {a, b};
      pair<Point, Point> pair2 = {b, a};
      if (find(visited_pairs.begin(), visited_pairs.end(), pair1) !=
          visited_pairs.end()) {
        continue;
      }
      if (find(visited_pairs.begin(), visited_pairs.end(), pair2) !=
          visited_pairs.end()) {
        continue;
      }
      visited_pairs.insert(pair1);

      auto antinodes = get_two_antinodes(a, b);
      Point a1 = antinodes.first, a2 = antinodes.second;

      if (node_in_bound(a1, H, W)) {
        antinodes_at.insert(a1);
      }
      if (node_in_bound(a2, H, W)) {
        antinodes_at.insert(a2);
      }
    }
  }

  return antinodes_at.size();
}

int part2() {
  string line;
  ifstream input("../data/input8.txt");

  vector<string> grid;

  if (input.is_open()) {
    while (getline(input, line)) {
      grid.push_back(line);
    }
    input.close();
  }

  int H = grid.size();
  int W = grid[0].size();

  map<char, vector<Point>> antennas;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (grid[i][j] == '.')
        continue;
      antennas[grid[i][j]].push_back({i, j});
    }
  }

  set<Point> antinodes_at;

  for (auto keyval : antennas) {
    vector<Point> points = keyval.second;

    vector<pair<Point, Point>> pairs;

    for (size_t i = 0; i < points.size(); i++) {
      for (size_t j = 0; j < points.size(); j++) {
        if (i == j)
          continue;

        pairs.push_back({points[i], points[j]});
      }
    }

    set<pair<Point, Point>> visited_pairs;

    for (auto p : pairs) {
      Point a = p.first;
      Point b = p.second;

      pair<Point, Point> pair1 = {a, b};
      pair<Point, Point> pair2 = {b, a};
      if (find(visited_pairs.begin(), visited_pairs.end(), pair1) !=
          visited_pairs.end()) {
        continue;
      }
      if (find(visited_pairs.begin(), visited_pairs.end(), pair2) !=
          visited_pairs.end()) {
        continue;
      }
      visited_pairs.insert(pair1);

      auto antinodes = get_two_antinodes(a, b);
      Point a1 = antinodes.first, a2 = antinodes.second;

      while (node_in_bound(a1, H, W) || node_in_bound(a2, H, W) ||
             node_in_bound(a, H, W) || node_in_bound(b, H, W)) {
        if (node_in_bound(a1, H, W)) {
          antinodes_at.insert(a1);
        }
        if (node_in_bound(a2, H, W)) {
          antinodes_at.insert(a2);
        }
        if (node_in_bound(a, H, W)) {
          antinodes_at.insert(a);
        }
        if (node_in_bound(b, H, W)) {
          antinodes_at.insert(b);
        }

        Point new_a1 = get_two_antinodes(a1, a).first;
        a = a1;
        a1 = new_a1;

        Point new_a2 = get_two_antinodes(b, a2).second;
        b = a2;
        a2 = new_a2;
      }
    }
  }

  return antinodes_at.size();
}
