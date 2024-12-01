from dataclasses import dataclass
from itertools import product
import re

@dataclass(init=True)
class Colors:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __repr__(self) -> str:
        return f"Color(red={self.red}, green={self.green}, blue={self.blue})"
    
    def get_power(self) -> int:
        return self.red * self.green * self.blue

data = []

with open("input2.txt", 'r') as fp:
    data = fp.read()

class Game:
    def __init__(self, game_id: int, sets: "list[Colors]") -> "Game":
        self.id = int(game_id)
        self.sets = sets

    def __repr__(self) -> str:
        return f"Game {self.id}: {self.sets}"
    
    def get_minimum_balls(self) -> "Colors":
        reds, greens, blues = [], [], []
        for s in self.sets:
            reds.append(s.red)
            greens.append(s.green)
            blues.append(s.blue)

        return Colors(red=max(reds), green=max(greens), blue=max(blues))


def parse_input(data: str) -> "list[Game]":
    games: "list[Game]" = []
    for line in data.split("\n"):
        out = re.match(r"(Game (\d+):) ([\d \w+, ;]+)", line)

        game_id = out.group(2)
        setline = out.group(3).split("; ")

        sets: "list[Colors]" = []

        for s in setline:
            balls = Colors(red=0, green=0, blue=0)
            clrs = s.split(", ")
            for c in clrs:
                setattr(balls, c.split(' ')[1], int(c.split(' ')[0]))

            sets.append(balls)

        games.append(Game(game_id, sets))
    return games

games = parse_input(data)
print(games)

answer = 0

for g in games:
    power = g.get_minimum_balls().get_power()
    answer += power

print(answer)