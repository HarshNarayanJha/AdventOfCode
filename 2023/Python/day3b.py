
class Grid:
  def __init__(self, data: str):
    self.grid = data.split("\n")
    self.all_numbers = self.recover_numbers()
    
  def get_tile(self, row: int, col: int):
    return self.grid[row][col]
  
  def get_symbols_coords(self, symbols: "list[str]"):
    coords = []
    for r, row in enumerate(self.grid):
      for c, ch in enumerate(row):
        if ch in symbols:
          coords.append((r, c))
          
    return coords
    
  def get_all_symbols_coords(self):
    from string import punctuation
    return self.get_symbols_coords(punctuation.replace('.', ''))
    
  def get_adjacent_numbers(self, row, col):
    numbers = []
    adjacent_coords = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    for adj in adjacent_coords:
      # print(self.get_tile(row+adj[0], col+adj[1]), self.get_tile(row+adj[0], col+adj[1]).isdigit())
      if self.get_tile(row+adj[0], col+adj[1]).isdigit():
        num = self.get_adjacent_number(row+adj[0], col+adj[1])
        if num:
          numbers.append(num)
    
    return numbers
  
  def get_adjacent_number(self, row: int, col: int):
    for coords in self.all_numbers:
      if (row, col) in coords:
        return self.all_numbers.pop(coords)
  
  def recover_numbers(self):
    all_numbers = {}
    for r, row in enumerate(self.grid):
      current_number = ""
      current_coords = []
      for c, ch in enumerate(row+'.'):
        if not ch.isdigit():
          if current_number.isnumeric():
            all_numbers[tuple(current_coords)] = int(current_number)
          current_number = ""
          current_coords = []
        else:
          current_number += ch
          current_coords.append((r, c))

    return all_numbers

    
data = None
with open('input3.txt', 'r') as fp:
  data = fp.read()
  
  
grid = Grid(data)
# pprint.pprint(grid.all_numbers, sort_dicts=False)

symbols = grid.get_symbols_coords(['*'])

answer = 0

for s in symbols:
  # print(grid.get_tile(*s))
  numbers = grid.get_adjacent_numbers(*s)
  # print(grid.get_tile(*s), numbers)
  if len(numbers) == 2:
    answer += numbers[0] * numbers[1]

print(answer)