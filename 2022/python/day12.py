"""
# AIM: To find the shortest path between the lowest and the highest elevated points (S and E) on a given heightmap
With keeping certain rules in mind :)
# INPUT: A file called 'heightmap.txt' in the this folder
# OUTPUT: A file called 'path_<steps>.txt' with the shortest path and no. of steps indicated
"""

from string import ascii_lowercase

class Step:
    def __init__(self, frm, to, dir):
        self.frm = frm
        self.to = to
        self.dir = dir

    def __repr__(self) -> str:
        return f"{self.frm} -> {self.to} {self.dir}"

class Heightmap:
    def __init__(self) -> None:
        self.map = []
        self.row = 0
        self.col = 0
        self.current_elevation = -1

    def load(self, lines: "list[str]"):
        for line in lines:
            self.map.append(list(line.replace("\n", "")))

    def print(self):
        print(self.map)

    def print9x9(self):
        matrix = [[], [], []]
        if self.col == 0:
            for i in self.map[self.row-1][self.col:self.col+2]:
                matrix[0].append(i)
            for i in self.map[self.row][self.col:self.col+2]:
                matrix[1].append(i)
            for i in self.map[self.row+1][self.col:self.col+2]:
                matrix[2].append(i)
        elif self.row == 0:
            for i in self.map[self.row][self.col-1:self.col+2]:
                matrix[1].append(i)
            for i in self.map[self.row+1][self.col-1:self.col+2]:
                matrix[2].append(i)
        elif self.row == 0 and self.col == 0:
            for i in self.map[self.row][self.col:self.col+2]:
                matrix[1].append(i)
            for i in self.map[self.row+1][self.col:self.col+2]:
                matrix[2].append(i)
        else:
            for i in self.map[self.row-1][self.col-1:self.col+2]:
                matrix[0].append(i)
            for i in self.map[self.row][self.col-1:self.col+2]:
                matrix[1].append(i)
            for i in self.map[self.row+1][self.col-1:self.col+2]:
                matrix[2].append(i)
        print("----------")
        for m in matrix:
            print(*m)

    def _search_for(self, char) -> "tuple(int, int)":
        for i, r in enumerate(self.map):
            if char in r:
                return i, r.index(char)

    def get_start(self, char="S") -> "tuple(int, int)":
        return self._search_for(char)
    
    def get_end(self, char="E") -> "tuple(int, int)":
        return self._search_for(char)

    def get_pos(self) -> "tuple(int, int)":
        return self.row, self.col
    
    def get_current_char(self) -> str:
        return self.map[self.row][self.col]

    def get_target_elevation(self, row, col) -> int:
        char = self.map[row][col]
        return ascii_lowercase.find(char)
    
    def set_pos(self, row, col) -> None:
        self.row = row
        self.col = col
    
    def move_up(self) -> "tuple(int, int)":
        if abs(self.current_elevation - self.get_target_elevation(self.row-1, self.col)) in (1, 0):
            self.row -= 1
            self.current_elevation = self.get_target_elevation(self.row, self.col)
            return Step((self.row+1, self.col),(self.row, self.col), self.move_up)
        # print("Target elevation is unreachable")
    def move_down(self) -> "tuple(int, int)":
        if abs(self.current_elevation - self.get_target_elevation(self.row+1, self.col)) in (1, 0):
            self.row += 1
            self.current_elevation = self.get_target_elevation(self.row, self.col)
            return Step((self.row-1, self.col),(self.row, self.col), self.move_down)
    def move_left(self) -> "tuple(int, int)":
        if abs(self.current_elevation - self.get_target_elevation(self.row, self.col-1)) in (1, 0):
            self.col -= 1
            self.current_elevation = self.get_target_elevation(self.row, self.col)
            return Step((self.row, self.col+1),(self.row, self.col), self.move_left)
    def move_right(self) -> "tuple(int, int)":
        if abs(self.current_elevation - self.get_target_elevation(self.row, self.col+1)) in (1, 0):
            self.col += 1
            self.current_elevation = self.get_target_elevation(self.row, self.col)
            return Step((self.row, self.col-1),(self.row, self.col), self.move_right)

    def move_to_upper_elevation(self, next_elevation):
        # print(next_elevation)
        choices = []
        if self.get_target_elevation(self.row, self.col+1) == next_elevation:
            if not last_dir == self.move_left:
                choices.append(self.move_right)
        if self.get_target_elevation(self.row+1, self.col) == next_elevation:
            if not last_dir == self.move_up:
                choices.append(self.move_down)
        if self.get_target_elevation(self.row-1, self.col) == next_elevation:
            if not last_dir == self.move_down:
                choices.append(self.move_up)
        if self.get_target_elevation(self.row, self.col-1) == next_elevation:
            if not last_dir == self.move_right:
                choices.append(self.move_left)
        
        if len(choices) == 1:
            return choices[0]()
        elif len(choices) > 1:
            print("Many choices", choices)
            # ind = int(input())
            return choices[-1]()
        elif len(choices) == 0:
            return self.move_to_upper_elevation(self.current_elevation)
            
Map = Heightmap()
with open('temp.txt', 'r') as f:
    Map.load(f.readlines())

Map.set_pos(*Map.get_start())
drow, dcol = Map.get_end()

Map.print()
# Map.print9x9()

steps = []
last_dir = None

while not Map.get_current_char() == "E":
    Map.print9x9()
    step = Map.move_to_upper_elevation(Map.current_elevation+1)
    if step is None:
        break
    steps.append(step)
    last_dir = step.dir
    print(step)

for s in steps: print(s)
print(Map.current_elevation)