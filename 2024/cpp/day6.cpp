#include <algorithm>
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
  ifstream input("../data/input6.txt");

  vector<string> maze;

  int start_x = 0, start_y = 0;

  if (input.is_open()) {

    int line_no = 0;
    while (getline(input, line)) {
      auto c = find(line.begin(), line.end(), '^');

      if (c != line.end()) {
        start_x = line_no;
        start_y = c - line.begin();
      }
      maze.push_back(line);

      line_no += 1;
    }
    input.close();
  }

  int height = maze.size();
  int width = maze[0].size();

  vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
  int direction = 0;

  int x = start_x, y = start_y;

  set<pair<int, int>> visited;
  visited.insert({x, y});

  while (true) {
    int dx = directions[direction].first;
    int dy = directions[direction].second;

    int tx = x + dx;
    int ty = y + dy;

    if (!((tx < height && tx >= 0) && (ty < width && ty >= 0))) {
      break;
    }

    if (maze[tx][ty] == '#') {
      // rotate right 90deg
      direction = (direction + 1) % 4;
    } else {
      x = tx;
      y = ty;
      visited.insert({x, y});
    }
  }

  return visited.size();
}

int part2() {
  string line;
  ifstream input("../data/input6.txt");

  vector<string> maze;

  int start_x = 0, start_y = 0;

  if (input.is_open()) {

    int line_no = 0;
    while (getline(input, line)) {
      auto c = find(line.begin(), line.end(), '^');

      if (c != line.end()) {
        start_x = line_no;
        start_y = c - line.begin();
      }
      maze.push_back(line);

      line_no += 1;
    }
    input.close();
  }

  int height = maze.size();
  int width = maze[0].size();

  int loop_count = 0;

  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {

      if (maze[i][j] == '#')
        continue;
      if (maze[i][j] == '^')
        continue;

      maze[i][j] = '#';

      vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
      int direction = 0;

      int x = start_x, y = start_y;

      set<pair<int, pair<int, int>>> visited;
      visited.insert({direction, {x, y}});

      while (true) {
        int dx = directions[direction].first;
        int dy = directions[direction].second;

        int tx = x + dx;
        int ty = y + dy;

        if (!((tx < height && tx >= 0) && (ty < width && ty >= 0))) {
          break;
        }

        if (maze[tx][ty] == '#') {
          // rotate right 90deg
          direction = (direction + 1) % 4;
        } else {
          x = tx;
          y = ty;

          if (visited.count({direction, {x, y}}) != 0) {
            loop_count++;
            break;
          }
          visited.insert({direction, {x, y}});
        }
      }

      maze[i][j] = '.';
    }
  }
  return loop_count;
}
