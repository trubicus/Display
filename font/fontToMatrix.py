abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for slovo in abeceda:
	f1 = open("originali/"+slovo+".txt", "r")
	f2 = open("matrix/"+slovo+".txt", "w")
	l=[]
	l = [line for line in f1]
	for char in range(6):
		for ln in range(7):
			print "char %d, ln %d, slovo %s, string %s" %(char, ln, slovo, l[ln])
			if l[ln][char] == "o":
				f2.write("1")
			else:
				f2.write("0") 
		f2.writelines("\n")
	f1.close()
	f2.close()
