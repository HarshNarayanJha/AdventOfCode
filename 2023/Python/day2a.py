from dataclasses import dataclass
import re

@dataclass(init=True)
class Colors:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __repr__(self) -> str:
        return f"Color(red={self.red}, green={self.green}, blue={self.blue})"

data = []

with open("input2.txt", 'r') as fp:
    data = fp.read()

class Game:
    def __init__(self, game_id: int, sets: "list[Colors]") -> "Game":
        self.id = int(game_id)
        self.sets = sets

    def __repr__(self) -> str:
        return f"Game {self.id}: {self.sets}"
    
    def check_if_sets_valid(self, set: "Colors") -> "bool":
        if any([s.red > set.red or s.blue > set.blue or s.green > set.green for s in self.sets]):
            return False
        return True


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

posed_condition = Colors(red=12, green=13, blue=14)

answer = 0

for g in games:
    if g.check_if_sets_valid(posed_condition): answer += g.id

print(answer)