import fileinput

cd = {}
with open("POSTags_PTB_Universal_Linux.txt") as f:
	for line in f:
		(key, val) = line.split()
		cd[key] = val

with fileinput.FileInput('pos_test.txt.pos.nltk.univ', inplace=True) as file:
	for line in file:
		check = False
		for key in reversed(sorted(cd.keys())):
			if (key in line) and (check == False):
				check = True 
				print(line.replace(key, cd[key]))
		if not check: print(line)

