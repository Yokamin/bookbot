# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Features

- Counts the total number of words in the book.
- Counts the frequency of each character (case-insensitive).
- Displays the characters sorted by frequency, from highest to lowest.
- Ignores non-alphabetical characters in the final report.
- Accepts any text file as input via command-line argument.

### Usage

1. Place your text file (e.g., `frankenstein.txt`) anywhere on your system.

   **Example text:** [Frankenstein from Project Gutenberg](https://www.gutenberg.org/cache/epub/41445/pg41445.txt)


2. Run the script from the command line, providing the path to the book file as an argument:

```bash
python3 main.py path/to/your/book.txt
```
For example:
```bash
python3 main.py books/frankenstein.txt
```

### Example Output

```yaml
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```