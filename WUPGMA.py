# Input and start params
pgma = [i for i in input().split()]
wu = pgma[1]
matrix_side = int(pgma[0])
start = 1
long = len(pgma[2::])
trinagle = {}
number = 2
leaves = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
leaves = leaves[:matrix_side:]


# Creating a dictionary

while long>0:
    for j in range(start, matrix_side):
        trinagle[(leaves[start-1], leaves[j])] = int(pgma[number])
        long -= 1
        number += 1
    start += 1
answer = ""


answer = {}
distance = {}

if wu == "WPGMA":
    while len(trinagle) > 0:

# Searching for minimal pair

        minimal = min(trinagle.values())
        for key in trinagle.keys():
            if trinagle[key] == minimal:
                pair = key
                break
        pmi = min(*pair)
        pma = max(*pair)

        if pair[0] in distance and pair[1] in distance:
            answer[f"{pair[0]}{pair[1]}"] = f"({answer[pair[0]]}:{round(minimal / 2 - distance[pair[0]], 2)},{answer[pair[1]]}:{round(minimal / 2 - distance[pair[1]], 2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
        elif pair[0] in distance and pair[1] not in distance:
            answer[f"{pair[0]}{pair[1]}"] = f"({answer[pair[0]]}:{round(minimal / 2 - distance[pair[0]], 2)},{pair[1]}:{round(minimal / 2,2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
        elif pair[1] in distance and pair[0] not in distance:
            answer[f"{pair[0]}{pair[1]}"] = f"({pair[0]}:{round(minimal / 2,2)},{answer[pair[1]]}:{round(minimal / 2 - distance[pair[1]], 2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
        else:
            answer[f"{pair[0]}{pair[1]}"] = f"({pair[0]}:{round(minimal / 2,2)},{pair[1]}:{round(minimal / 2, 2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
            

# Recomputing the matrix

        del trinagle[pair]
        for i in leaves:
            if pmi < i < pma:
                trinagle[(f"{pmi+pma}",i)] = (trinagle[(pmi, i)] + trinagle[(i, pma)])/2
                del trinagle[(pmi, i)]
                del trinagle[(i, pma)]
            elif i < pmi:
                trinagle[(i, f"{pmi+pma}")] = (trinagle[(i, pmi)] + trinagle[(i, pma)])/2
                del trinagle[(i, pmi)]
                del trinagle[(i, pma)]
            elif i > pma:
                trinagle[(f"{pmi+pma}", i)] = (trinagle[(pmi, i)] + trinagle[(pma, i)])/2
                del trinagle[(pmi, i)]
                del trinagle[(pma, i)]
        leaves.remove(pmi)
        leaves.remove(pma)
        leaves.append(f"{pmi+pma}")
        leaves = sorted(leaves)
    print(answer[leaves[0]])

    
    
elif wu == "UPGMA":
    while len(trinagle) > 0:
        
        
# Searching for minimal pair

        minimal = min(trinagle.values())
        for key in trinagle.keys():
            if trinagle[key] == minimal:
                pair = key
                break
        pmi = min(*pair)
        pma = max(*pair)

        if pair[0] in distance and pair[1] in distance:
            answer[f"{pair[0]}{pair[1]}"] = f"({answer[pair[0]]}:{round(minimal / 2 - distance[pair[0]], 2)},{answer[pair[1]]}:{round(minimal / 2 - distance[pair[1]], 2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
        elif pair[0] in distance and pair[1] not in distance:
            answer[f"{pair[0]}{pair[1]}"] = f"({answer[pair[0]]}:{round(minimal / 2 - distance[pair[0]], 2)},{pair[1]}:{round(minimal / 2,2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
        elif pair[1] in distance and pair[0] not in distance:
            answer[f"{pair[0]}{pair[1]}"] = f"({pair[0]}:{round(minimal / 2,2)},{answer[pair[1]]}:{round(minimal / 2 - distance[pair[1]], 2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)
        else:
            answer[f"{pair[0]}{pair[1]}"] = f"({pair[0]}:{round(minimal / 2,2)},{pair[1]}:{round(minimal / 2, 2)})"
            distance[f"{pair[0]}{pair[1]}"] = round(minimal / 2, 2)


# Recomputing the matrix

        del trinagle[pair]
        for i in leaves:
            if pmi < i < pma:
                trinagle[(f"{pmi+pma}",i)] = (trinagle[(pmi, i)]*len(pmi) + trinagle[(i, pma)]*len(pma))/(len(pmi)+len(pma))
                del trinagle[(pmi, i)]
                del trinagle[(i, pma)]

            elif i < pmi:
                trinagle[(i, f"{pmi+pma}")] = (trinagle[(i, pmi)]*len(pmi) + trinagle[(i, pma)]*len(pma))/(len(pmi)+len(pma))
                del trinagle[(i, pmi)]
                del trinagle[(i, pma)]

            elif i > pma:
                trinagle[(f"{pmi+pma}", i)] = (trinagle[(pmi, i)]*len(pmi) + trinagle[(pma, i)]*len(pma))/(len(pmi)+len(pma))
                del trinagle[(pmi, i)]
                del trinagle[(pma, i)]

        leaves.remove(pmi)
        leaves.remove(pma)
        leaves.append(f"{pmi+pma}")
        leaves = sorted(leaves)
    print(answer[leaves[0]])
