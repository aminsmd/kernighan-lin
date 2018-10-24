from math import *
import numpy as np

no_nodes = input()
nodes = list(range(int(no_nodes)))
marked = list(np.zeros(int(no_nodes)))
pA = list(range(int(int(no_nodes)/2)))
pB = list(range(int(int(no_nodes)/2), int(no_nodes)))
E = list(np.zeros(int(no_nodes)))
I = list(np.zeros(int(no_nodes)))
D = list(np.zeros(int(no_nodes)))
cost_matrix = []

for i in range(int(no_nodes)):
    r = input().split()
    for i in range(len(r)):
        r[i] = int(r[i])
    cost_matrix.append(r)

for j in pA:
    for k in pA:
        I[j] += cost_matrix[j][k]
    for l in pB:
        E[j] += cost_matrix[j][l]
    D[j] = abs(E[j]-I[j])

for j in pB:
    for k in pB:
        I[j] += cost_matrix[j][k]
    for l in pA:
        E[j] += cost_matrix[j][l]
    D[j] = abs(E[j]-I[j])
flag = 0

while flag == 0:

    gain = []
    g = []
    for i in pA:
        for j in pB:
            if marked[int(i)] or marked[int(j)]:
                g.append(-1000)
            else:
                g.append(D[i] + D[j] - 2*cost_matrix[int(i)][int(j)])
        gain.append(g)
        g = []

    m = 0
    sw = []
    for i in range(len(gain)):
        for j in range(len(gain[i])):
            if gain[i][j] > m:
                m = gain[i][j]
                sw = i, j

    if m == 0:
        print(pA)
        print(pB)
        cost = 0
        for i in pA:
            for j in pB:
                cost += cost_matrix[i][j]
        print(cost)
        flag = 1
    else:
        marked[int(pA[int(sw[0])])] = 1
        marked[int(pB[int(sw[1])])] = 1
        for v in pA:
            D[v] += (2 * int(cost_matrix[v][pA[sw[0]]]) - 2 * int(cost_matrix[v][pB[sw[1]]]))
        for v in pB:
            D[v] += (2 * int(cost_matrix[v][pB[sw[1]]]) - 2 * int(cost_matrix[v][pA[sw[0]]]))
        pA[sw[0]], pB[sw[1]] = pB[sw[1]], pA[sw[0]]




