#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <regex>

std::string digits = "1234567890";

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