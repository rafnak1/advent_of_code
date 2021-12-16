with open('input') as f:
    xv = list(map(int, f.read().split(',')))

costs = {}
for i in range(min(xv), max(xv)):
    for x in xv:
        costs[i] = costs.get(i, 0) + abs(x-i)

print(min(costs.values()))
