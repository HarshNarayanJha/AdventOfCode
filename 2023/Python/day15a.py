with open("input15.txt", "r") as fp:
    words = fp.read().split(",")

print(words)

current_values = [0] * len(words)

for i, word in enumerate(words):
    for ch in word:
        current_values[i] += ord(ch)
        current_values[i] *= 17
        current_values[i] = current_values[i] % 256

print(current_values)
print(sum(current_values))