# Importing numpy for working with matrices
# Computing len of input RNA

import numpy as np
rna = input()
l_rna = len(rna)
loop = 3
compl = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
dic = {'A':0, 'U':1, 'G':2, 'C':3}

# Creating and filling the matrix
nusinov = np.eye(l_rna, dtype="int")-1
for i in range(l_rna):
    for j in range(l_rna):
        if j - i <= 3:
            nusinov[i][j] = 0
for i in range(l_rna):
    for j in range(l_rna):
        if j < i:
            nusinov[i][j] = -100

# Realizing algorithm

i = 0
j = loop + 1
m = j
while i != 0 or j <= l_rna - 1:
    while j < l_rna:
        for k in range(i,j):
            value_exp = max((compl[dic[rna[i]]][dic[rna[j]]] + nusinov[i + 1][j - 1]), (nusinov[i][k] + nusinov[k + 1][j]))
            if nusinov[i][j] < value_exp:
                nusinov[i][j] = value_exp
        i += 1
        j += 1
    i = 0
    j = m + 1
    m += 1


# Function for identifying reverse way

i = 0
j = l_rna - 1
def way(i, j, loop):
    if compl[dic[rna[i]]][dic[rna[j]]] == 1 and (nusinov[i][j] - nusinov[i+1][j-1] == 1):
        print(i+1, j+1, end=" ")
        i += 1
        j -= 1
        if abs(i-j) > loop:
            way(i, j, loop)
    else:
        for k in range(j-1,i-1,-1):
            if nusinov[i][j] == nusinov[i][k] + nusinov[k+1][j]:
                if abs(i-k) > loop:
                    way(i, k, loop)
                if abs(k+1-j) > loop:
                    way(k+1, j, loop)
                break
# Finding matched pairs

way(0, l_rna-1, loop)
