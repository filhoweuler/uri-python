
line = input()
line = line.split(" ")

A = int(line[0])
B = int(line[1])

if A%B == 0 or B%A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
