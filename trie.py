from collections import namedtuple

Result = namedtuple('Result', ['is_prefix','is_word'])

class Trie:
    """a trie structure for incremental word searching"""

    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word):
        """add a word to the trie"""

        if word == "":
            self.is_word = True
            return

        letter, the_rest = word[0], word[1:]

        if not self.children.has_key(letter):
            self.children[letter] = Trie()

        self.children[letter].insert(the_rest)

    def find(self, word):
        """search for a word in the trie"""

        if word == "":
            return Result(len(self.children)>0, self.is_word)

        letter, the_rest = word[0], word[1:]

        if not self.children.has_key(letter):
            return Result(False, False) # Not in the structure.

        return self.children[letter].find(the_rest)

if __name__ == '__main__':
    t = Trie()
    t.insert("cat")
    t.insert("car")
    t.insert("back")
    print 'found "cat"?', t.find("cat")
    print 'found "truck"?', t.find("truck")
    print 'found "ba"?', t.find("ba")
