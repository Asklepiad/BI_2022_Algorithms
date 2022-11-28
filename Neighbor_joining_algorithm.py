# Inputting data and saving basic values

input_list = [i for i in input().split()]
matrix_side = int(input_list[0])
leaves = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
leaves = leaves[:matrix_side:]
distance = {}
c=1


# Computing Hamming distance

while c <= matrix_side:
    for d in range(c+1, len(input_list)):
        hamming = 0
        for nucleotide in range(len(input_list[1])):
            if input_list[c][nucleotide] != input_list[d][nucleotide]:
                hamming += 1
        distance[(leaves[c-1], leaves[d-1])] = hamming
    c += 1
answer = {}


# Computing minimum

while len(distance) > 1:
    
    minimal = 10000000
    matrix_minus = distance.copy()
    for key in distance.keys():
        sum_i, sum_j = 0, 0
        for k in leaves:
            if k != key[0] and k > key[0]:
                sum_i += distance[(key[0], k)]
            elif k != key[0] and k < key[0]:
                sum_i += distance[(k, key[0])]
            if k != key[1] and k > key[1]:
                sum_j += distance[(key[1], k)]
            elif k != key[1] and k < key[1]:
                sum_j += distance[(k, key[1])]
        matrix_minus[key] = (matrix_side - 2) * distance[key] - sum_i - sum_j
        if matrix_minus[key] < minimal:
            minimal = matrix_minus[key]
            minimal_value = distance[key]
            key_minimal = key
            sum_i_const = sum_i
            sum_j_const = sum_j
    
    # Computing the distances between two chosen nodes and new node

    delta1 = round((minimal_value / 2) + (1 / (2 * (matrix_side - 2))) * (sum_i_const - sum_j_const),1)
    delta2 = round(minimal_value - delta1,1)
    pmi = key_minimal[0]
    pma = key_minimal[1]
    
    
    
    if pmi in answer and pma in answer:
        answer[f"{pmi}{pma}"] = f"({answer[pmi]}:{round(delta1, 1)},{answer[pma]}:{round(delta2, 1)})"
    elif pmi in answer and pma not in answer:
        answer[f"{pmi}{pma}"] = f"({answer[pmi]}:{round(delta1, 1)},{pma}:{round(delta2, 1)})"
    elif pma in answer and pmi not in answer:
        answer[f"{pmi}{pma}"] = f"({pmi}:{round(delta1, 1)},{answer[pma]}:{round(delta2, 1)})"
    else:
        answer[f"{pmi}{pma}"] = f"({pmi}:{round(delta1, 1)},{pma}:{round(delta2, 1)})"
    
    
    
    # Recomputing of the matrix
    
    for i in leaves:
        if pmi < i < pma:
            distance[(f"{pmi+pma}",i)] = (1 / 2) * (distance[(pmi, i)] + distance[(i, pma)] - distance[key_minimal])
            del distance[(pmi, i)]
            del distance[(i, pma)]
            del matrix_minus[(pmi, i)]
            del matrix_minus[(i, pma)]

        elif i < pmi:
            distance[(i, f"{pmi+pma}")] = (1 / 2) * (distance[(i, pmi)] + distance[(i, pma)] - distance[key_minimal])
            del distance[(i, pmi)]
            del distance[(i, pma)]
            del matrix_minus[(i, pmi)]
            del matrix_minus[(i, pma)]

        elif i > pma:
            distance[(f"{pmi+pma}", i)] = (1 / 2) * (distance[(pmi, i)] + distance[(pma, i)] - distance[key_minimal])
            del distance[(pmi, i)]
            del distance[(pma, i)]
            del matrix_minus[(pmi, i)]
            del matrix_minus[(pma, i)]

    del distance[key_minimal]
    del matrix_minus[key_minimal]
    leaves.remove(pmi)
    leaves.remove(pma)
    leaves.append(f"{pmi+pma}")
    leaves = sorted(leaves)
    matrix_side -= 1    
    
# Computing last value

for key in distance.keys():
    key_last = key

pmi = key_last[0]
pma = key_last[1]
delta = distance[key_last]
    
if pmi in answer and pma in answer:
    answer[f"{pmi}{pma}"] = f"({answer[pmi]}:{round(delta / 2, 1)},{answer[pma]}:{round(delta / 2, 1)})"
elif pmi in answer and pma not in answer:
    answer[f"{pmi}{pma}"] = f"({answer[pmi]}:{round(delta / 2, 1)},{pma}:{round(delta / 2, 1)})"
elif pma in answer and pmi not in answer:
    answer[f"{pmi}{pma}"] = f"({pmi}:{round(delta / 2, 1)},{answer[pma]}:{round(delta / 2, 1)})"
else:
    answer[f"{pmi}{pma}"] = f"({pmi}:{round(delta / 2, 1)},{pma}:{round(delta / 2, 1)})"

print(answer[f"{pmi}{pma}"])
