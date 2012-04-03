import re

def build_graph(tokenized):
    graph = Graph()

    tokens = filter(lambda t: t!='', re.split(r'(\w\+*\**)', tokenized))
    for token in tokens:
        graph.insert(token[0], token[1:]) # 'Q', '**'

    return graph

class Graph:
    """A container object for the nodes in a scramble graph"""

    LETTER_VALUES = {'A':1,'B':4,'C':4,'D':2,'E':1,'F':4,'G':3,'H':3,'I':1,
        'J':10,'K':5,'L':2,'M':4,'N':2,'O':1,'P':4,'QU':10,'R':1,'S':1,'T':1,
        'U':2,'V':5,'W':4,'X':8,'Y':3,'Z':10}

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def insert(self, letter, modifier=None):
        """insert a letter into the next available position"""

        data_len = len(self.data)
        if data_len >= 17:
            raise Exception

        if modifier == '':
            modifier = None

        if letter == 'Q':
            letter = 'QU'

        index = (data_len/4,data_len%4)
        self[index] = {
            'letter': letter,
            'value': Graph.LETTER_VALUES[letter],
            'modifier': modifier
        }

    def neighbors(self, c, r):
        """generates a list of neighboring coordinate pairs"""

        for nc in xrange(max(0,c-1),min(4,c+2)):
            for nr in xrange(max(0,r-1),min(4,r+2)):
                if nr == r and nc == c: continue
                yield nc,nr

    def path_word(self, path):
        """translates a path into a word"""

        return ''.join([self[node]['letter'] for node in path])

    def path_score(self, path):
        """scores a given path, taking modifiers into account"""

        score, path_multipliers = 0, []

        for node in path:

            if self[node]['modifier'] == '+':
                score += 2*self[node]['value']

            elif self[node]['modifier'] == '++':
                score += 3*self[node]['value']

            elif self[node]['modifier'] == '*':
                path_multipliers.append(2)
                score += self[node]['value']

            elif self[node]['modifier'] == '**':
                path_multipliers.append(3)
                score += self[node]['value']

            else:
                score += self[node]['value']

        score = reduce(lambda s,m: s*m, [score]+path_multipliers)
        return score
