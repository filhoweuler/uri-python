entrada = str(input())
entrada = entrada.split(" ")

# print(entrada[0])
# print(entrada[1])

n = int(entrada[0])
m = int(entrada[1])

for i in range(n):
    linha = str(input())
    linha = linha.split(" ")
    for j in range(m):
        mat[i][j] = linha[m]

for i in range(n):
    for j in range(m):
        print(mat[i][j])