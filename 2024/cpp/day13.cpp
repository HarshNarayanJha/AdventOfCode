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
long int part2();

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
    long int x1 = m[0].first, y1 = m[0].second;
    long int x2 = m[1].first, y2 = m[1].second;
    long int x3 = m[2].first, y3 = m[2].second;

    // x1*a + x2*b = x3
    // y1*a + y2*b = y3
    // solve for a, b using Cramer's rule
    long int det = x1 * y2 - x2 * y1;
    if (det != 0) {
      long int det_a = x3 * y2 - x2 * y3;
      long int det_b = x1 * y3 - x3 * y1;

      long int a = det_a / det;
      long int b = det_b / det;

      if ((det_a % det == 0) && (det_b % det == 0) && a >= 0 && b >= 0) {
        long int total_cost = a * 3 + b;
        if (total_cost > 0) {
          cost += total_cost;
        }
      }
    }
  }

  return cost;
}

long int part2() {
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

        t.first = stol(x) + 10000000000000;
        t.second = stol(y) + 10000000000000;
      }
    }

    machine.push_back(a);
    machine.push_back(b);
    machine.push_back(t);
    machines.push_back(machine);
    machine.clear();
    input.close();
  }

  long int cost = 0;

  for (const auto &m : machines) {
    long int x1 = m[0].first, y1 = m[0].second;
    long int x2 = m[1].first, y2 = m[1].second;
    long int x3 = m[2].first, y3 = m[2].second;

    // x1*a + x2*b = x3
    // y1*a + y2*b = y3
    // solve for a, b using Cramer's rule
    long int det = x1 * y2 - x2 * y1;
    if (det != 0) {
      long int det_a = x3 * y2 - x2 * y3;
      long int det_b = x1 * y3 - x3 * y1;

      long int a = det_a / det;
      long int b = det_b / det;

      if ((det_a % det == 0) && (det_b % det == 0) && a >= 0 && b >= 0) {
        long int total_cost = a * 3 + b;
        if (total_cost > 0) {
          cost += total_cost;
        }
      }
    }
  }

  return cost;
}
