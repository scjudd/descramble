#!/usr/bin/env python2

import os
import argparse
import wx

import marisa_trie

from descramble.graph import build_graph
from descramble.core import solve
from descramble.gui import SolutionsFrame

def default_wordlist():
    paths = ['words.marisa', '/usr/share/descramble/words.marisa']

    for path in paths:
        if os.path.exists(path): return path

    return 'words.marisa'

parser = argparse.ArgumentParser(
    description="Solve Scramble with Friends puzzles like a pro.",
    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-w', dest='wordlist', type=argparse.FileType('r'),
    default=default_wordlist(),
    help='specify the word list')

parser.add_argument(dest='tokenized', metavar='PUZZLE',
    help='e.g., "H**ENCS++IMHN++ORASP++EN", where\n'
         '\t+  = double letter\n'
         '\t++ = triple letter\n'
         '\t*  = double word\n'
         '\t** = triple word\n'
         '\tNOTE: \'Qu\' is expressed as \'Q\'')

args = vars(parser.parse_args())

trie = marisa_trie.Trie()
trie.read(args['wordlist'])

graph = build_graph(args['tokenized'])

results = solve(graph, trie)
sorted_results = sorted(results.iteritems(), key=lambda w:w[1]['score'],
    reverse=True)

app = wx.App(False)
frame = SolutionsFrame(None, 'Descramble')
frame.SetResults(sorted_results)
frame.Show(True)
app.MainLoop()
