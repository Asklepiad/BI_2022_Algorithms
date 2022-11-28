import numpy as np
x = input()
y = input()
gap = -5
prematr = [4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2, 0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2, \
          -2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3, -1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1, 2, 0, 0, -1, -2, -3, -2, \
          -2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3, 0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3, -2, \
           -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2,-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1, -1, -3, \
           -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2,-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1, 1, -2, -1,-1, -1, -3, \
           -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1,-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2, -1, -3, -1, -1, -4, -2, \
           -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3,-1, -3,  0,  2, -3, -2, 0, -3,  1, -2, 0, 0, -1, 5,  1,  0, -1, -2, -2, -1,-1, -3, -2,  0, -3, -2,  0, \
           -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2, 1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2, 0, -1, -1, -1, -2, -2, -2, -1,\
           -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2, 0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1,-3, -2, -4, -3,  1, -2, -2, -3, -3,\
           -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2,-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
dic = {"A":0,  "C":1,  "D":2,  "E":3,  "F":4,  "G":5,  "H":6,  "I":7,  "K":8,  "L":9,  "M":10,  "N":11,  "P":12,  "Q":13,  "R":14,  "S":15,  "T":16,  "V":17,  "W":18,  "Y":19}
matr = np.reshape(prematr,(20,20))


# Start data: length of sequences, importing numpy, building of matrix

n = len(x)
m = len(y)
mat = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for j in range(m+1):
    mat[0][j] = j*gap
for i in range(n+1):
    mat[i][0] = i*gap



# Filling matrix with weights

for i in range(1, n+1):
    for j in range(1, m+1):
        diag = mat[i-1][j-1]+matr[dic[x[i-1]]][dic[y[j-1]]]
        mat[i][j] = max(diag, mat[i-1][j]+gap, mat[i][j-1]+gap)


# Output sequences

a1=[]
a2=[]


# Searching the right way
while n>0 or m>0:
    vert = mat[n-1][m]+gap
    hor = mat[n][m-1]+gap
    diag1 = mat[n-1][m-1]+matr[dic[x[n-1]]][dic[y[m-1]]]
    
    if mat[n][m] == diag1:
        a1.append(x[n-1])
        a2.append(y[m-1])
        n -= 1
        m -= 1    
    elif mat[n][m] == hor and (m>0 or m>=n):
        a1.append("-")
        a2.append(y[m-1])
        m -= 1
    elif mat[n][m] == vert:
        a1.append(x[n-1])
        a2.append("-")
        n -= 1


#Outputs

print(*a1[::-1], sep="")
print(*a2[::-1], sep="")
