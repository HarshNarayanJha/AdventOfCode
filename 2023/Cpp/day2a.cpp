#include <iostream>
#include <fstream>
#include <vector>
#include <regex>


std::vector<std::string> split(std::string str, char delim) {
    std::vector<std::string> result;
    std::stringstream line(str);
    std::string s;

    while( getline(line, s, delim)) {
        result.push_back(s);
    }

    return result;
}

class colors {
    public:
        colors(int red, int green, int blue) : red(red), green(green), blue(blue) {}
        colors() {}

        void print() {
            std::cout << "Color(red=" << red << ", green=" << green << ", blue=" << blue << ")" << std::endl;
        }

        void set(int r, int g, int b) {
            red = r;
            green = g;
            blue = b;
        }

        void set_r(int r) {
            red = r;
        }
        void set_b(int b) {
            blue = b;
        }
        void set_g(int g) {
            green = g;
        }

    private:
        int red = 0;
        int green = 0;
        int blue = 0;

    friend class Game;
};

class Game {
    public:

        Game(int game_id, std::vector<colors> sets): game_id(game_id), color_sets(sets) {}

        Game() {}

        void set_game_id(int game_id) {
            this->game_id = game_id;
        }

        void set_sets(std::vector<colors> sets) {
            this->color_sets = sets;
        }

        void push_back_color_set(colors set) {
            this->color_sets.push_back(set);
        }

        int get_game_id() {
            return game_id;
        }

        void print() {
            std::cout << "Game: " << game_id << std::endl;
        }

        bool check_if_sets_valid(colors set) {
            bool flag = true;

            for (int i = 0; i < color_sets.size(); ++i) {
                if (color_sets.at(i).red > set.red) flag = false;
                if (color_sets.at(i).green > set.green) flag = false;
                if (color_sets.at(i).blue > set.blue) flag = false;
            }

            return flag;
        }

    private:
        int game_id;
        std::vector<colors> color_sets;
        int num_sets;
};

int main() {
    std::vector<std::string> lines;
    std::string line;

    std::ifstream InputRead("../input2.txt");

    while (std::getline(InputRead, line)) {
        lines.push_back(line);
    }

    InputRead.close();

    std::vector<Game> games;

    std::smatch match;

    for (auto &line : lines) {
        if (std::regex_match(line, match, std::regex("(Game (\\d+):) ([\\d \\w+, ;]+)"))) {
            int game_id = stoi(match[2]);
            std::string colors_text = match[3];

            Game game;
            game.set_game_id(game_id);

            auto split_colors_text = split(colors_text, ';');

            for (auto &set : split_colors_text) {

                colors cols;
                auto split_set = split(set, ',');

                for (auto &col : split_set) {

                    if (col.find("red") != std::string::npos) {
                        // std::cout << "red" << std::stoi(col) << std::endl;
                        cols.set_r(std::stoi(col));
                    }
                    if (col.find("green") != std::string::npos) {
                        // std::cout << "green" << std::stoi(col) << std::endl;
                        cols.set_g(std::stoi(col));
                    }
                    if (col.find("blue") != std::string::npos) {
                        // std::cout << "blue" << std::stoi(col) << std::endl;
                        cols.set_b(std::stoi(col));
                    }
                }
                
                game.push_back_color_set(cols);
            }

            games.push_back(game);
        }
    }

    // std::cout << games.size();

    colors posed_condition = colors(12, 13, 14);

    int answer = 0;

    for (int i = 0; i < games.size(); ++i) {
        if (games[i].check_if_sets_valid(posed_condition)) {
            answer += games[i].get_game_id();
        }
    }

    std::cout << "Answer: " << answer << std::endl;
}


