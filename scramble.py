from collections import deque
from trie import Trie, build_trie

def path_word(graph, path):
    """translates a path into a word"""

    return ''.join([graph[n][0] for n in path])

def path_score(graph, path):
    """scores a given path, taking modifiers into account"""

    score, path_multipliers = 0, []

    for node in path:

        if graph[node][-1] == '2L':
            score += 2*graph[node][-2]

        elif graph[node][-1] == '3L':
            score += 3*graph[node][-2]

        elif graph[node][-1] == '2W':
            path_multipliers.append(2)
            score += graph[node][-2]

        elif graph[node][-1] == '3W':
            path_multipliers.append(3)
            score += graph[node][-2]

        else:
            score += graph[node][-1]

    score = reduce(lambda s,m: s*m, [score]+path_multipliers)
    return score

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

            word = path_word(graph,path) + path_word(graph,[neighbor])
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

def solve(graph, trie):
    """solve the puzzle. returns the best-scoring path for each word"""

    found = {}

    for path in search(graph, trie):

        word = path_word(graph, path)
        score = path_score(graph, path)

        if found.has_key(word):
            if found[word]['score'] < score:
                found[word]['path'] = path
                found[word]['score'] = score
            continue

        found[word] = { 'path': path, 'score': score }

    return found

if __name__ == '__main__':

    graph = {}
    graph[(0,0)] = ('S',1)
    graph[(1,0)] = ('R',1)
    graph[(2,0)] = ('QU',10,'3W')
    graph[(3,0)] = ('A',1)
    graph[(0,1)] = ('A',1)
    graph[(1,1)] = ('S',1,'2L')
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

    with open('TWL_2006_ALPHA.txt') as word_list:
        trie = build_trie(word_list)

    results = solve(graph, trie)
    sorted_results = sorted(results.iteritems(), key=lambda w:w[1]['score'],
                            reverse=True)

    for result in sorted_results:
        print result
