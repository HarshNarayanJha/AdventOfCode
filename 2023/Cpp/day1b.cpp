#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>
#include <regex>

std::map<std::string, std::string> digits {
    {"one", "o1e"},
    {"two", "t2o"},
    {"three", "t3e"},
    {"four", "f4r"},
    {"five", "f5e"},
    {"six", "s6x"},
    {"seven", "s7n"},
    {"eight", "e8t"},
    {"nine", "n9e"},
};

int main()
{
    std::vector<std::string> lines;
    std::vector<int> numbers;

    std::string line;

    std::ifstream InputRead;

    InputRead.open("../input1.txt");

    while (std::getline(InputRead, line)) {
        lines.push_back(line);
    }

    InputRead.close();

    for (int i = 0; i < lines.size(); ++i)
    {
        char first = 'x';
        char last = 'x';
        std::string line = lines[i];

        for (auto &p : digits)
        {
            std::cout << p.first << " " << p.second << std::endl;
            line = std::regex_replace(line, std::regex(p.first), p.second);
        }

        line = std::regex_replace(line, std::regex("[A-z]"), "");

        std::string thenumbers;
        
        for (int j = 0; j < line.size(); ++j)
        {
            char c = line[j];
            if (first == 'x') first = c;

            last = c;
        }

        if (last == 'x') last = first;

        thenumbers.push_back(first);
        thenumbers.push_back(last);

        numbers.push_back(std::stoi(thenumbers));
    }

    int32_t sum = std::accumulate(numbers.begin(), numbers.end(), 0);

    std::cout << "Solution: " << sum << std::endl;

    return 0;
}