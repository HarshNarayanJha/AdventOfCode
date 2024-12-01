data = []

with open("input1.txt", "r") as fp:
	data = fp.readlines()

numbers = []

for line in data:
	first, last = -1, -1

	for char in line:
		if char.isdigit() and first == -1:
			first = char

		elif char.isdigit():
			last = char

	if last == -1:
		last = first

	# print(first, last)

	numbers.append(int(first+last))

print(sum(numbers))