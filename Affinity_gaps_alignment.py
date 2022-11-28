import numpy as np
inp = input().split()
x = inp[0]
y = inp[1]
match = int(inp[2])
mismatch = int(inp[3])
gap_open = int(inp[4])
gap_cont = int(inp[5])
n = len(x)
m = len(y)

mat_vert = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for j in range(m+1):
    mat_vert[0][j] = -10000
for i in range(n+1):
    mat_vert[i][0] = gap_open + i*gap_cont
mat_vert[0][0] = 0

mat_diag = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for j in range(m+1):
    mat_diag[0][j] = -10000
for i in range(n+1):
    mat_diag[i][0] = -10000
mat_diag[0][0] = 0

mat_hor = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for i in range(n+1):
    mat_hor[i][0] = -10000
for j in range(m+1):
    mat_hor[0][j] = gap_open + j*gap_cont
mat_hor[0][0] = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if x[i-1] == y[j-1]:
            diag = match
        else:
            diag = mismatch
        gap_combo = gap_open + gap_cont
        mat_vert[i][j] = max(mat_vert[i-1][j]+gap_cont, mat_diag[i-1][j]+gap_combo, mat_hor[i-1][j]+gap_combo)
        mat_diag[i][j] = max(mat_vert[i-1][j-1]+diag, mat_diag[i-1][j-1]+diag, mat_hor[i-1][j-1]+diag)
        mat_hor[i][j] = max(mat_vert[i][j-1]+gap_combo, mat_diag[i][j-1]+gap_combo, mat_hor[i][j-1]+gap_cont)

a1=[]
a2=[]
st = max(mat_vert[n][m], mat_diag[n][m], mat_hor[n][m])
if max(mat_vert[n][m], mat_diag[n][m], mat_hor[n][m]) == mat_diag[n][m]:
    a1.append(x[n-1])
    a2.append(y[m-1])
    flag = "d"
    n-=1
    m-=1
elif max(mat_vert[n][m], mat_diag[n][m], mat_hor[n][m]) == mat_vert[n][m]:
    a1.append(x[n-1])
    a2.append("_")
    flag = "v"
    n-=1
elif max(mat_vert[n][m], mat_diag[n][m], mat_hor[n][m]) == mat_hor[n][m]:
    a1.append("_")
    a2.append(y[m-1])
    flag = "h"
    m-=1
    
while n>0 or m>0: 
    if flag == "d":
        if x[n] == y[m]:
            const = match
        else:
            const = mismatch
        prev = mat_diag[n+1][m+1]
        if mat_diag[n][m]+const == prev:
            a1.append(x[n-1])
            a2.append(y[m-1])
            flag = "d"
            n -= 1
            m -= 1
        elif mat_vert[n][m]+const == prev:
            a1.append(x[n-1])
            a2.append("_")
            flag = "v"
            n -= 1
        elif mat_hor[n][m]+const == prev:
            a1.append("_")
            a2.append(y[m-1])
            flag = "h"
            m -= 1
        
    elif flag == "v":
        prev = mat_vert[n+1][m]
        if mat_diag[n][m]+gap_open+gap_cont == prev:
            a1.append(x[n-1])
            a2.append(y[m-1])
            flag = "d"
            n -= 1
            m -= 1
        elif mat_vert[n][m]+gap_cont == prev:
            a1.append(x[n-1])
            a2.append("_")
            flag = "v"
            n -= 1
        elif mat_hor[n][m]+gap_open+gap_cont == prev:
            a1.append("_")
            a2.append(y[m-1])
            flag = "h"
            m -= 1
    
    elif flag == "h":
        prev = mat_hor[n][m+1]
        
        if mat_diag[n][m]+gap_open+gap_cont == prev:
            a1.append(x[n-1])
            a2.append(y[m-1])
            flag = "d"
            n -= 1
            m -= 1
        elif mat_vert[n][m]+gap_open+gap_cont == prev:
            a1.append(x[n-1])
            a2.append("_")
            flag = "v"
            n -= 1
        elif mat_hor[n][m]+gap_cont == prev:
            a1.append("_")
            a2.append(y[m-1])
            flag = "h"
            m -= 1   
print(st, end=" ")
print(*a1[::-1], sep = "", end=" ")
print(*a2[::-1], sep = "")    
