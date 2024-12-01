import re

data = ""

with open("input1.txt", "r") as fp:
	data = fp.read().strip()

digits = {
	"one": "o1e",
	"two": "t2o",
	"three": "t3e", 
	"four": "f4r", 
	"five": "f5e", 
	"six": "s6x", 
	"seven": "s7e", 
	"eight": "e8t",
	"nine": "n9e"
	}
	
def replace(data):
	for k, v in digits.items():
		data = data.replace(k, v)
	return data
	

def calculate(data):
	return [int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", data).split("\n")]
		
print(sum(calculate(data)))
print(sum(calculate(replace(data))))