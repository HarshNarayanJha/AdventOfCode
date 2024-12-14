

with open('./2022/datastream_buffer.txt', 'r') as f:
    data = f.read()
data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

start = -1
for i, c in enumerate(data, 1):
    if i < len(data) - 4:
        upto_4 = [c, data[i], data[i+1], data[i+2]]
        print(upto_4)
        if all(m != n for a, m in enumerate(upto_4) for b, n in enumerate(upto_4) if a != b):
            print(i)
