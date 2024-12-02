#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int part1();
int part2();

int main() {
  cout << part1() << endl;
  cout << part2() << endl;
}

bool is_report_safe(vector<int>::iterator start, vector<int>::iterator end) {
  vector<int> report(start, end);

  vector<bool> increasing_safes;
  vector<bool> decreasing_safes;

  for (size_t i = 0; i < report.size() - 1; i++) {
    if (report.at(i) < report.at(i + 1) &&
        (report.at(i + 1) - report.at(i)) <= 3) {
      increasing_safes.push_back(true);
    } else {
      increasing_safes.push_back(false);
    }

    if (report.at(i) > report.at(i + 1) &&
        (report.at(i) - report.at(i + 1)) <= 3) {
      decreasing_safes.push_back(true);
    } else {
      decreasing_safes.push_back(false);
    }
  }

  if (count(increasing_safes.begin(), increasing_safes.end(), false) == 0) {
    return true;
  }

  if (count(decreasing_safes.begin(), decreasing_safes.end(), false) == 0) {
    return true;
  }

  return false;
}

int part1() {
  string line;
  ifstream input;
  input.open("../data/input2.txt", ios::in);

  vector<vector<int>> reports;

  if (input.is_open()) {
    while (getline(input, line)) {
      stringstream ss(line);

      string s;
      vector<int> levels;

      while (ss >> s) {
        levels.push_back(stoi(s));
      }
      reports.push_back(levels);
    }
    input.close();
  }

  int safe_reports = 0;

  for (vector<int> report : reports) {
    if (is_report_safe(report.begin(), report.end())) {
      safe_reports++;
    }
  }

  return safe_reports;
}

int part2() {
  string line;
  ifstream input;
  input.open("../data/input2.txt", ios::in);

  vector<vector<int>> reports;

  if (input.is_open()) {
    while (getline(input, line)) {
      stringstream ss(line);

      string s;
      vector<int> levels;

      while (ss >> s) {
        levels.push_back(stoi(s));
      }
      reports.push_back(levels);
    }
    input.close();
  }

  int safe_reports = 0;

  for (vector<int> &report : reports) {
    if (is_report_safe(report.begin(), report.end())) {
      safe_reports++;
    } else {
      for (size_t i = 0; i < report.size(); i++) {
        vector<int> check_report;
        check_report.insert(check_report.end(), report.begin(),
                            report.begin() + i);
        check_report.insert(check_report.end(), report.begin() + i + 1,
                            report.end());

        if (is_report_safe(check_report.begin(), check_report.end())) {
          safe_reports++;
          break;
        }
      }
    }
  }

  return safe_reports;
}
