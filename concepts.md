# Essential info:

Python este o specificație
 (există mai multe implementări)

este interpretat

în Python totul (totul!) este un obiect

este whitespace-sensitive (nu avem acolade!)

în Python _totul_ este o referință

vine cu "batteries included"

Python este orientat către "Duck Typing":
  - if it walks like a duck and quacks like a duck
    it's good enough for me



# Essential debugging tools

print()
type()
help()

# basic data types:

int
float
str
bool

list  # mutable
tuple # immutable

## sequences:
str, list, tuple

- sunt iterabile
- acceptă acces după index
- acceptă acces după slice
- au lungime: suportă funcția len()
- au metodele .count() și .index()
- acceptă operatorul "in"


# Concepte:

"reprezentare" a obiectului
fiecare operator are o metodă în spate

iterator vs. iterable

iterabile:
 - sequences
 - range()
 - iteratori: filter(), itertools.repeat()

toți iteratorii sunt iterabili
nu toate iterabilele sunt iteratori

venv = virtual environment

# Diverse:

PEP-8: the style guide:
https://peps.python.org/pep-0008/

string formatting:
https://docs.python.org/3/library/string.html#format-examples

# Base exceptions:

NameError: variabila nu există
TypeError: data type-uri nepotrivite
           argumente lipsă la funcție
ValueError: când valoarea "nu se potrivește"
IndexError: nu există item-ul cu indexul respectiv (la sequences)
KeyError:   nu există cheia respectivă (în dicționar)

# Useful things to install:

To install things, în shell de sistem:

$ pip install package_name

sau, dacă pip nu e în PATH:

$ python -m pip install requests

Useful things:

- ipython
- rich
- requests


# Utile în VSCode:

Ctrl+F5     run file
Shift+Enter execute selection
Ctrl+/      comment selection or current line


# Essential wisdom:

There are 2 hard problems in computing:
- naming things
- cache invalidation
- off-by-one errors
