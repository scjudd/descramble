from collections import deque

def bfs(start, graph, trie):
    """iterative breadth-first search"""

    queue = deque([[start]])

    while queue:

        path = queue.popleft()

        for neighbor in set(graph.neighbors(*path[-1])) - set(path):

            word = unicode(graph.path_word(path) + graph[neighbor]['letter'])

            if word in trie:
                yield path+[neighbor]

            if trie.keys(word):
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

        word = graph.path_word(path)
        score = graph.path_score(path)

        if found.has_key(word):
            if found[word]['score'] < score:
                found[word]['path'] = path
                found[word]['score'] = score
            continue

        found[word] = { 'path': path, 'score': score }

    return found
