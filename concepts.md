# Essential info:

Python este o specificație
 (există mai multe implementări)

este interpretat

în Python totul (totul!) este un obiect

este whitespace-sensitive (nu avem acolade!)

în Python _totul_ este o referință

vine cu "batteries included"

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
- au lungime: suportă funcția len()
- au metodele .count() și .index()


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

# Diverse:

PEP-8: the style guide
https://peps.python.org/pep-0008/

# Base exceptions:

NameError: variabila nu există
TypeError: data type-uri nepotrivite
           argumente lipsă la funcție
ValueError: când valoarea "nu se potrivește"


# Utile în VSCode:

Ctrl+F5  run file
Shift+Enter execute selection
