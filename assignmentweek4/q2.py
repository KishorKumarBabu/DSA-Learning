def onehop(l):
    from collections import defaultdict
    adjacency=defaultdict(set)
    for start,end in l:
        adjacency[start].add(end)
    result=set()
    for i in list(adjacency.keys()):
        for k in adjacency[i]:
            for j in adjacency[k]:
                if i!=j:
                    result.add((i,j))
    return sorted(result)
print(onehop([(2,3),(1,2)]))