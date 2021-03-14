import fileinput

cd = {}
with open("ChunkDict.txt") as f:
	for line in f:
		(key, val) = line.split()
		cd[key] = val

with fileinput.FileInput('wsj_0010_sample.txt.std.nltk', inplace=True) as file:
	for line in file:
		check = False
		for key in reversed(sorted(cd.keys())):
			if (key in line) and (check == False):
				check = True 
				print(line.replace(key, cd[key]))
		if not check: print(line)

