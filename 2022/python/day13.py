
class Pair:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		
	def __repr__(self):
		return f"Pair {self.left} and {self.right}"
		
	def check_lists(self, l, r):
		
		for i, j in zip(l, r):
			print(f"Compare {i} and {j}")
			
			if isinstance(i, int) and isinstance(j, int):
				if i < j:
					print("Left Side is Smaller, so inputs are in the right order")
					return True
				elif i > j:
					print("Right Side is Smaller, so inputs are not in the right order")
					return False
				elif i == j: continue
			
			elif isinstance(i, list) and isinstance(j, list):
				result = self.check_lists(i, j)
				if not result is None: return result
			
			elif isinstance(i, list) and isinstance(j, int):
				print(f"Mixed types; convert right to {[j]} and retry comparison!")
				print(f"Compare {i} and {[j]}")
				result = self.check_lists(i, [j])
				if not result is None: return result
			
			elif isinstance(i, int) and isinstance(j, list):
				print(f"Mixed types; convert left to {[i]} and retry comparison!")
				print(f"Compare {[i]} and {j}")
				result = self.check_lists([i], j)
				if not result is None: return result
			
		if len(l) < len(r):
			print("Left side ran out of items, so inputs are in the right order")
			return True
		elif len(l) > len(r):
			print("Right side ran out of items, so inputs are not in the right order")
			return False
		elif len(l) == len(r): pass
	
	def is_right_order(self):
		print(f"Compare {self.left} and {self.right}")
		return self.check_lists(self.left, self.right)
		
#print(Pair(a, b).is_right_order())
pairs = []

with open("2022/distress_signal.txt", "r") as f:
	data = f.readlines()
temp = []
for l in data:
	l = l.replace("\n", "")
	if not l:
		pairs.append(Pair(temp[0], temp[1]))
		temp.clear()
		continue
	temp.append(eval(l))
	
#print(pairs)

rights = []

for i, p in enumerate(pairs):
	if p.is_right_order():
		print(i+1)
		rights.append(i+1)
	print()

print()
print()
# print(f"Right indices are {rights}")
# print(f"Sum is {sum(rights)}")

# Part 2

from functools import cmp_to_key

all_packets = [j for i in pairs for j in [i.left, i.right]] + [[[2]], [[6]]]
all_packets.sort(key=cmp_to_key(Pair([], []).check_lists), reverse=True)
print()
print((all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1))