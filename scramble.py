#!/usr/bin/env python2

from collections import deque
from graph import build_graph
from trie import build_trie

def bfs(start, graph, trie):
    """iterative breadth-first search"""

    queue = deque([[start]])

    while queue:

        path = queue.popleft()

        for neighbor in set(graph.neighbors(*path[-1])) - set(path):

            word = graph.path_word(path) + graph[neighbor]['letter']
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

        word = graph.path_word(path)
        score = graph.path_score(path)

        if found.has_key(word):
            if found[word]['score'] < score:
                found[word]['path'] = path
                found[word]['score'] = score
            continue

        found[word] = { 'path': path, 'score': score }

    return found

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(
        description="Solve Scramble with Friends puzzles like a pro.",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(dest='tokenized', metavar='PUZZLE',
        help='e.g., "H**ENCS++IMHN++ORASP++EN", where\n'
             '\t+  = double letter\n'
             '\t++ = triple letter\n'
             '\t*  = double word\n'
             '\t** = triple word\n'
             '\tNOTE: \'Qu\' is expressed as \'Q\'')

    graph = build_graph(vars(parser.parse_args())['tokenized'])

    with open('resources/word_lists/TWL_2006_ALPHA.txt') as word_list:
        trie = build_trie(word_list)

    results = solve(graph, trie)
    sorted_results = sorted(results.iteritems(), key=lambda w:w[1]['score'],
        reverse=True)

    import wx
    from gui import SolutionsFrame

    app = wx.App(False)
    frame = SolutionsFrame(None, 'Scramble Solver')
    frame.SetResults(sorted_results)
    frame.Show(True)
    app.MainLoop()
