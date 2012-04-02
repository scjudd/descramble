from collections import deque

def neighbors(c,r):
    for nc in xrange(max(0,c-1),min(4,c+2)):
        for nr in xrange(max(0,r-1),min(4,r+2)):
            if nr == r and nc == c: continue
            yield nc,nr

def dfs(start, path=[]):
    """recursive depth-first search"""
    if len(path) == 0:
        path.append(start)
    nodes = set(n for n in neighbors(*start)) - set(path)
    for node in nodes:
        for sub_path in dfs(node, path+[node]):
            yield sub_path
    yield path

def bfs(start):
    """iterative breadth-first search"""
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        yield path
        for n in set(neighbors(*path[-1])) - set(path):
            queue.extend([path+[n]])

if __name__ == '__main__':

    data = {}
    data[(0,0)] = ('S',1)
    data[(1,0)] = ('R',1)
    data[(2,0)] = ('Qu',10)
    data[(3,0)] = ('A',1)
    data[(0,1)] = ('A',1)
    data[(1,1)] = ('S',1)
    data[(2,1)] = ('I',1)
    data[(3,1)] = ('T',1)
    data[(0,2)] = ('I',1)
    data[(1,2)] = ('D',2)
    data[(2,2)] = ('E',1)
    data[(3,2)] = ('N',2)
    data[(0,3)] = ('F',4)
    data[(1,3)] = ('S',1)
    data[(2,3)] = ('A',1)
    data[(3,3)] = ('P',4)

    for c in xrange(0,4):
        for r in xrange(0,4):
            print data[(c,r)][0], [data[n][0] for n in neighbors(c,r)]

    print '*** starting depth-first search ***'
    for path in dfs((0,0)):
        print path

    print '*** starting breadth-first search ***'
    for path in bfs((0,0)):
        print path
