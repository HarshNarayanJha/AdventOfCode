#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;
using Point = pair<long int, long int>;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

int part1() {
  string line;
  ifstream input("../data/input13.txt");

  vector<vector<Point>> machines;

  if (input.is_open()) {

    vector<Point> machine;
    Point a;
    Point b;
    Point t;
    while (getline(input, line)) {
      if (line.empty()) {
        machine.push_back(a);
        machine.push_back(b);
        machine.push_back(t);
        machines.push_back(machine);
        machine.clear();
        continue;
      }

      if (line.find("Button A") != string::npos) {
        string temp, part;
        istringstream ss(line);
        getline(ss, temp, ':');
        getline(ss, part);

        string x, y;
        ss.clear();
        ss.str(part);
        getline(ss, x, ',');
        getline(ss, y);

        ss.clear();
        ss.str(x);
        getline(ss, temp, '+');
        getline(ss, x, '+');

        ss.clear();
        ss.str(y);
        getline(ss, temp, '+');
        getline(ss, y, '+');

        a.first = stoi(x);
        a.second = stoi(y);

      } else if (line.find("Button B") != string::npos) {
        string temp, part;
        istringstream ss(line);
        getline(ss, temp, ':');
        getline(ss, part);

        string x, y;
        ss.clear();
        ss.str(part);
        getline(ss, x, ',');
        getline(ss, y);

        ss.clear();
        ss.str(x);
        getline(ss, temp, '+');
        getline(ss, x, '+');

        ss.clear();
        ss.str(y);
        getline(ss, temp, '+');
        getline(ss, y, '+');

        b.first = stoi(x);
        b.second = stoi(y);

      } else if (line.find("Prize") != string::npos) {
        string temp, part;
        istringstream ss(line);
        getline(ss, temp, ':');
        getline(ss, part);

        string x, y;
        ss.clear();
        ss.str(part);
        getline(ss, x, ',');
        getline(ss, y);

        ss.clear();
        ss.str(x);
        getline(ss, temp, '=');
        getline(ss, x, '=');

        ss.clear();
        ss.str(y);
        getline(ss, temp, '=');
        getline(ss, y, '=');

        t.first = stoi(x);
        t.second = stoi(y);
      }
    }

    machine.push_back(a);
    machine.push_back(b);
    machine.push_back(t);
    machines.push_back(machine);
    machine.clear();
    input.close();
  }

  int cost = 0;

  for (const auto &m : machines) {
    Point a = m[0];
    Point b = m[1];
    Point p = m[2];

    int min_cost = INT_MAX;
    int best_a = 0, best_b = 0;
    int curr_x = 0, curr_y = 0;

    for (int bp = 0; bp < 100; bp++) {
      int curr_b_x = b.first * bp;
      int curr_b_y = b.second * bp;

      for (int ap = 0; ap < 100; ap++) {
        curr_x = curr_b_x + a.first * ap;
        curr_y = curr_b_y + a.second * ap;

        if (curr_x == p.first && curr_y == p.second) {
          int total_cost = ap * 3 + bp * 1;
          if (total_cost < min_cost) {
            min_cost = total_cost;
            best_a = ap;
            best_b = bp;
          }
        }
      }
    }

    if (min_cost != INT_MAX) {
      cost += min_cost;
    }
  }

  return cost;
}

int part2() { return 0; }
