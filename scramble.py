from collections import deque
from trie import Trie

def neighbors(c,r):
    """generates a list of neighboring coordinate pairs"""
    for nc in xrange(max(0,c-1),min(4,c+2)):
        for nr in xrange(max(0,r-1),min(4,r+2)):
            if nr == r and nc == c: continue
            yield nc,nr

def bfs(start, graph, trie):
    """iterative breadth-first search"""
    queue = deque([[start]])
    while queue:
        path = queue.popleft()

        for neighbor in set(neighbors(*path[-1])) - set(path):

            word = ''.join([graph[n][0] for n in path]+[graph[neighbor][0]])
            result = trie.find(word)

            if result.is_word:
                yield path+[neighbor]

            if result.is_prefix:
                queue.extend([path+[neighbor]])

def search(graph, trie):
    """begin a series of breadth-first searches on every coordinate pair"""

    for c in xrange(0,4):
        for r in xrange(0,4):
            for path in bfs((c,r), graph, trie):
                yield path

def build_trie(fileObj):
    """parse a file containing a newline-separated list of words into
    a prefix tree"""

    trie = Trie()

    for word in fileObj.readlines():
        trie.insert(word.upper().strip())

    return trie

if __name__ == '__main__':

    graph = {}
    graph[(0,0)] = ('S',1)
    graph[(1,0)] = ('R',1)
    graph[(2,0)] = ('QU',10)
    graph[(3,0)] = ('A',1)
    graph[(0,1)] = ('A',1)
    graph[(1,1)] = ('S',1)
    graph[(2,1)] = ('I',1)
    graph[(3,1)] = ('T',1)
    graph[(0,2)] = ('I',1)
    graph[(1,2)] = ('D',2)
    graph[(2,2)] = ('E',1)
    graph[(3,2)] = ('N',2)
    graph[(0,3)] = ('F',4)
    graph[(1,3)] = ('S',1)
    graph[(2,3)] = ('A',1)
    graph[(3,3)] = ('P',4)

    for c in xrange(0,4):
        for r in xrange(0,4):
            print graph[(c,r)][0], [graph[n][0] for n in neighbors(c,r)]

    print '*** building trie ***'
    with open('TWL_2006_ALPHA.txt') as word_list:
        trie = build_trie(word_list)
    print '*** trie built! ***'


    print '*** starting breadth-first search ***'
    # TODO: only save the best-scoring path for each word
    found = []
    for path in search(graph, trie):
        word = ''.join([graph[n][0] for n in path])
        score = reduce(lambda x,y: x+y, [graph[n][1] for n in path])
        found.append({'word':word, 'path':path, 'score':score})
    found.sort(key=lambda w: w['score'], reverse=True)
    print '*** finished breadth-first search! ***'

    print '*** RESULTS ***'
    for f in found:
        print f['word'], f['score']
