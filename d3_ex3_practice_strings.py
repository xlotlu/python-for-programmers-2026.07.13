# Dat fiind numele de coloană
c = "####Name####"
# obțineți numele de coloană fără caracterele
# de padding.
c.strip('#')

# Dat fiind capul de tabel
h = "|####Name # etc####|#Age#|#####Address#####|"
# obțineți o listă cu numele coloanelor.
columns = []

for c in h.split('|')[1:-1]:
    columns.append(c.strip('#'))
columns


# side discussion: list comprehension

# creăm lista pătratelor numerelor de la 1 la 9
accumulator = []
for elem in range(5):
    accumulator.append(elem ** 2)

# rescrisă:
[
    elem ** 2
    for elem in range(5)
]

# next level:
# creăm lista pătratelor numerelor impare de la 1 la 9
accumulator = []
for elem in range(1, 10):
    if elem % 2:
        accumulator.append(elem ** 2)

# rescrisă:
[
    elem ** 2
    for elem in range(1, 10)
    if elem % 2
]


# înapoi la exemplu:
columns = []

for c in h.split('|')[1:-1]:
    columns.append(c.strip('#'))

# cu list comprehension:
[
    c.strip('#')
    for c in h.split('|')[1:-1]
]


# Scrieți o funcție ce replică funcționalitatea
# lui `str.startswith()`
def startswith(s, substr):
    return s[:len(substr)] == substr

# Scrieți o funcție ce replică funcționalitatea
# lui `str.removesuffix()`
def removesuffix(s, suffix):
    slen = len(substr)
    if s[-slen:] == suffix:
        return s[:-slen]
    return True

# [opțional, algoritmică] Scrieți o funcție
def padint(number, length):
    pass
# ce primind un număr întreg îl prefixează cu zero-uri
# până atinge lungimea dată.
# ex: padint(25, 4) --> "0025"
#
# faceți asta low-level, algoritmic, ignorând
# că există metodele `.rjust()` / `.zfill()`

def padint(number, length):
    number = str(number)

    if len(number) >= length:
        return number

    padding = length - len(number)
    return "0" * padding + number

# versiune one-linerish
def padint(number, length):
    number = str(number)
    # pentru că merge un string înmulțit cu număr negativ
    return "0" * (length - len(number)) + number


# Exercițiu
# scrieți o funcție
def get_words(txt):
    pass
# ce returnează o listă cu toate cuvintele
# din string-ul `txt`

# strategie?
# - ne definim "caracterele speciale"
# - înlocuim pe fiecare din ele cu spațiu
# - facem split

# cum construim bad chars?
# din range-uri
_BAD_CHAR_RANGES = (
    range(0, 32),
    range(33, 48),
    range(58, 65),
    range(91, 97),
    range(124, 128)
)

for _range in _BAD_CHAR_RANGES:
    for n in _range:
        BAD_CHARS.append(chr(n))

# echivalent, cu list comprehension

BAD_CHARS = [
   chr(n)
   for _range in _BAD_CHAR_RANGES
   for n in _range
]

# sau poate...
#import string
#BAD_CHARS = string.punctuation + string.whitespace

def get_words(txt):
    # înlocuim fiecare caracter special cu spațiu
    for chr in BAD_CHARS:
        txt = txt.replace(chr, " ")
    return txt.split()

# alternativ, eficient, implementat în C:
BAD_CHARS_TABLE = str.maketrans(
    "".join(BAD_CHARS),
    " " * len(BAD_CHARS)
)

def get_words(txt):
    return txt.translate(BAD_CHARS_TABLE).split()


print(
    get_words("""
        Eu sunt un text,
        deosebit, de lung
        cu multe @!% caractere &* speciale...
        unele (lipite de altele) și altele.
        și cu numere123 ce facem?
    """)
)


# 1. Scrieți o funcție
def get_seconds(timespec):
    pass
# ce calculează numărul de secunde din
# `timespec`, care va fi în format 'HH:MM:SS'

def get_seconds(timespec):
    hours, minutes, seconds = [int(part) for part in timespec.split(':')]
    # echivalent cu:
    hours, minutes, seconds = map(int, timespec.split(':'))

get_seconds('1:00:00') == 3600
get_seconds('2:01:00') == 7260


# 2. Îmbunătățiți funcția get_seconds()
# astfel încât să poată procesa
# `timespec` în format: 'HH' / 'HH:MM' / 'HH:MM:SS'

def get_seconds(timespec):
    try:
        parts = [int(part) for part in timespec.split(':')]
    except ValueError:
        raise ValueError(f'Invalid timespec: "{timespec}"')

    if not (1 <= len(parts) <= 3):
        raise ValueError(f'Invalid timespec: "{timespec}"')

    # we fill the remainder of parts with zeroes,
    # to account for all possibilities
    remainder = 3 - len(parts)
    parts += [0] * remainder

    hours, minutes, seconds = parts

    return hours * 3600 + minutes * 60 + seconds

get_seconds('1') == 3600
get_seconds('1:01') == 3660
get_seconds('1:01:01') == 3661
