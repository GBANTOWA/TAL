import fileinput

d = {}
with open("POSTags_PTB_Universal_Linux.txt") as f:
	for line in f:
		(key, val) = line.split()
		d[key] = val

with fileinput.FileInput('wsj_0010_sample.txt.pos.univ.nltk', inplace=True) as file:
	for line in file:
		check = False
		for key in reversed(sorted(d.keys())):
			if (key in line) and (check == False):
				check = True 
				print(line.replace(key, d[key]))

with fileinput.FileInput('wsj_0010_sample.pos.univ.ref', inplace=True) as file:
	for line in file:
		check = False
		for key in reversed(sorted(d.keys())):
			if (key in line) and (check == False):
				check = True 
				print(line.replace(key, d[key]))


