# salutare, dicționare

# Exercițiu: dată fiind structura de date
friends = [
    ['Jane', 20, ['reading', 'hiking', 'biking']],
    ['Mike', 17, ['hiking', 'fishing']],
    ['Anna', 25, []],
    ['Sam', 40, ['playing guitar']],
    ['Dan', 34, ['painting', 'reading']]
]

# transformați `friends` într-o listă de dicționare

fdicts = [
    dict(zip(['name', 'age', 'hobbies'], f))
    for f in friends
]
# lista este acum
[
    {'name': 'Jane', 'age': 20, 'hobbies': ['reading', 'hiking', 'biking']},
    {'name': 'Mike', 'age': 17, 'hobbies': ['hiking', 'fishing']},
    {'name': 'Anna', 'age': 25, 'hobbies': []},
    {'name': 'Sam', 'age': 40, 'hobbies': ['playing guitar']},
    {'name': 'Dan', 'age': 34, 'hobbies': ['painting', 'reading']}
]


#
# Exercițiu: dat fiind dicționarul
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
}
# în care cheia este numele persoanei din dataset-ul `friends`
# adăugați la fiecare dicționar de friend
# cheia "occupation" cu valoarea potrivită.

# Strategie:
# - iterăm prin fdicts
# - accesăm din fiecare dicționar cheia "name"
# - cu valoarea obținută facem lookup în occupations
# - și această valoare va fi ocupația omului curent

for fdict in fdicts:
    name = fdict["name"]
    occupation = occupations[name]
    fdict["occupation"] = occupation

for friend in fdicts: friend["occupation"] = occupations[friend["name"]]

# Ne-am făcut un prieten nou:
fdicts.append({
    "name": "Jay",
    "age": 50,
    "hobbies": ["running", "hiking"],
})

# "Jay" nu există în occupations.
# Strategii de tratat cu chei care nu există:

# 1) dacă _vrem_ întotdeauna o valoare, folosim .get()

for fdict in fdicts:
    name = fdict["name"]
    occupation = occupations.get(name)
    fdict["occupation"] = occupation

# 2) dacă _nu vrem_ o valoare:
# 2.1) cu excepție
for fdict in fdicts:
    name = fdict["name"]
    try:
        occupation = occupations[name]
    except KeyError:
        # ocupația nu există
        continue

    fdict["occupation"] = occupation

# 2.2) condițional
for fdict in fdicts:
    name = fdict["name"]

    if name in occupations:
        occupation = occupations[name]
        fdict["occupation"] = occupation


# Exercițiu:
# dat fiind noile ocupații, 
# cu persoane care nu există în friends.
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
    "Michaela": "polo player",
    "Georgie": "singer",
    "Shumiko": "salubrity engineer",
}

# abordați problema invers:
# iterați prin occupations și updatați elementul
# corect din `fdicts` cu ocupația respectivă.
#
# întrebare: cum puteți face asta fără să iterați
# prin `fdicts` pentru fiecare persoană?

# Strategie: ne folosim de un dicționar
# construit pe baza numelui:
# {
#    "Jane": friend
# }
friendsdict = {
    friend["name"]: friend
    for friend in fdicts
}

for name, occ in occupations.items():
    if name in friendsdict:
        friend = friendsdict[name]
        friend["occupation"] = occ


# Exercițiu:
# scrieți o funcție
def count_words(txt):
    pass
# ce primind string-ul `txt`, numără aparițiile
# fiecărui cuvânt din string și returnează
# un data type potrivit pentru a oferi și cuvântul și nr.-ul
#
# testați-o pe string-ul

s = """
  It was the best of times,
  it was the worst of times,
  it was the age of wisdom,
  it was the age of foolishness,
  it was the epoch of belief,
  it was the epoch of incredulity,
  it was the season of light,
  it was the season of darkness,
  it was the spring of hope,
  it was the winter of despair.
"""

from d3_ex3_practice_strings import get_words

# un dicționar nou în care împingem:
# iterăm for word in words
# dacă găsește cuvântul îi mai adăugăm +1
# și dacă nu găsește cuvântul adăugăm cuvântul cu valoare 1

def count_words(txt):
    counts = {}

    for word in get_words(txt):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(count_words(s))

# alternativ, folosind defaultdict:
from collections import defaultdict

def count_words(txt):
    counts = defaultdict(int)

    for word in get_words(txt):
        counts[word] += 1

    return counts
