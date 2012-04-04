Scramble Solver
===============

## Game Rules

1. No square may be used more than once.
2. Connected squares must be neighbors.
3. Connected squares must form a real word.

![Neighbors](http://img40.imageshack.us/img40/8409/neighbors.png)

## Searching

Searching is done using a [breadth-first search][wiki_bfs] algorithm.
For example:

<img src="http://img94.imageshack.us/img94/5025/83315660.png">
<img src="http://img407.imageshack.us/img407/7328/0010ek.png">
<img src="http://img195.imageshack.us/img195/6126/0001gm.png">

## Data Structure

Data will be parsed from a text file containing a list of newline-separated
words into a [prefix tree][wiki_trie] structure.

## Usage

python ./scramble.py "H\*\*ENCS++IMHN++ORASP++EN"

* + = double letter
* ++ = triple letter
* \* = double word
* \*\* = triple word

## Screenshot

This is a scaled and cropped screenshot taken from my iPad 1. It should not be
used for image processing.

![Scaled Screenshot](http://dumpon.us/media/uploads/scaled_screenshot.png)

[wiki_bfs]: http://en.wikipedia.org/wiki/Breadth-first_search
[wiki_trie]: http://en.wikipedia.org/wiki/Trie
