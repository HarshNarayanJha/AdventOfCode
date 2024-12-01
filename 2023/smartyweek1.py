addresses = ["14582 Christmas Tree Rd, Johnston City, IL, 62951", "23151 Christmas Dr, Denham Springs, LA, 70726", "745 W Ornament Ln, Santa Claus, IN, 47579", "203 N Santa Claus Ln, North Pole, AK, 99705"]

latlongs = [
	(37.806553,-88.983376),
	(30.406538,-90.861435),
	(38.10577, -86.943207),
	(64.755859, -147.354141)
	]
	
result = 0

for i, j in latlongs:
	result += int(i)
	result += int(j)
	
print(abs(result))