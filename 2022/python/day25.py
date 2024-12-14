with open('./2022/snafu.txt', 'r') as f:
    s = f.readlines()

# s = []
# for l in s_nums.strip().split("\n"):
# 	s.append(l)
	
nums = []
for l in s:
	num = 0
	for n, i in enumerate(l[::-1]):
		if i.isdigit():
			num += int(i) * 5**n
		elif i == "-":
			num += -1 * 5**n
		elif i == "=":
			num += -2 * 5**n
	nums.append(num)
			
print(sum(nums)) # 35798042807410
total = sum(nums)

# convert back to snafu