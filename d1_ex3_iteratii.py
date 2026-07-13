iterable = "un string"

#for element in iterable:
#    print("»", element)

lst = ["elem 1", "elem 2", 1, 2, 3, "etc."]

for elem in lst:
    print(elem)

for elem in range(15):
    print(elem)

# Exercițiu:
# creați o listă
# ce conține pătratele numerelor de la 1 la 10

# Pattern de acumulare:

#1. definesc obiectul final
lst = []

#2. iterez în sursă
for elem in range(1, 11):
    #3. calculăm rezultatul curent
    value = elem ** 2
    #4. acumulăm
    lst.append(value)
#5. gata
print(lst)

# Exercițiu:
# creați o listă
# ce conține pătratele numerelor impare de la 1 la 20

# Pattern de acumulare complet:

#1. definesc obiectul final
lst = []

#2. iterez în sursă
for elem in range(1, 11):
    #3. filtrare
    if elem % 2 == 1:
        #4. calculăm rezultatul curent
        value = elem ** 2
        #5. acumulăm
        lst.append(value)
#6. gata
print(lst)


# Exercițiu:
# cunoscând sintaxa de acces după index,
# dat fiind lista de orașe
cities = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Craiova',
 'Brașov',
 'Galați',
 'Ploiești',
 'Oradea',
 'Brăila',
 'Arad',
 'Sibiu',
 'Bacău',
 'Târgu Mureș',
 'Baia Mare',
 'Buzău',
 'Satu Mare',
 'Suceava',
]

# creați o listă nouă
# cu orașele care încep cu litera "B"
def _exercitiu():
    orase_cu_B = []

    for oras in cities:
        if oras[0] == "B":
            orase_cu_B.append(oras)
    
    print(orase_cu_B)
_exercitiu()

# Exercițiu:
# scrieți o funcție de forma
def filter_by_first_letter(iterable, letter, insensitive=False):
    pass # NO-OP statement
# ce returnează o listă cu elementele
# din `iterable` care încep cu `letter`,
# ținând cont de case-sensitive / case-insensitive matching

def filter_by_first_letter(iterable, letter, insensitive=False):
    # normalizăm input-ul după caz
    if insensitive:
        letter = letter.upper()

    resultat = []
    for oras in iterable:
        first_letter = oras[0]
        # normalizăm input-ul după caz
        if insensitive:
            first_letter = first_letter.upper()
                    
        if first_letter == letter:
            resultat.append(oras)

    return resultat
    

print(filter_by_first_letter(cities, "B", insensitive=True))


# Exercițiu:
# dată fiind lista de numere
l = [15, 22, 17]
# scrieți o funcție
def avg(iterable):
    pass
# ce returnează media numerelor din `iterable`.
# vă prefaceți că nu știți că există funcția `sum()`.


def avg(iterable):
    sum = 0
    for num in iterable:
        sum = sum + num
    return sum / len(iterable)

print(avg([15, 22, 17]))
print(avg(range(10)))


# Exercițiu:
# dată fiind lista de elemente de forma (name, distance)
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 400),
    ('Constanța', 225),
    ('Craiova', 230),
    ('Brașov', 180),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 600),
    ('Brăila', 200),
    ('Arad', 580),
    ('Sibiu', 275),
    ('Bacău', 300),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
    ('Buzău', 110),
    ('Satu Mare', 640),
    ('Suceava', 450),
]

# obțineți o listă nouă cu orașele
# cu distanță mai mică decât 300.
#
# scrieți o funcție ce primind ca argument lista
# și distanța de filtrare
# să returneze o listă nouă de forma celei inițiale.

def filter_by_distance(cities, dist):
    result = []
    for city in cities:
        if city[1] < dist:
            result.append(city)
    return result

filter_by_distance(cities, 300)


def filter_by_letter(cities, letter, insensitive=False):
    if insensitive:
        letter = letter.upper()

    resultat = []
    for element in cities:
        name = element[0]
        first_letter = name[0]
        if insensitive:
            first_letter = first_letter.upper()
                    
        if first_letter == letter:
            resultat.append(element)

    return resultat


filter_by_distance(filter_by_letter(cities, "C"), 300)


# Exercițiu: să filtrăm mai inteligent / pythonic
# folosim funcția filter

def filterer(elem):
    return elem[0][0] == "B"

for elem in filter(filterer, cities):
    print(elem)

# rescriem cu lambda:
filtered = filter(lambda elem: elem[0][0] == "B", cities)

for elem in filtered:
    print(elem)

#def custom_filter(elem):
#    return elem[0][0] == "B" and elem[1] < 300

# filtrare dublă:
filtered = filter(
    lambda elem: (
        elem[0][0] == "B"
        and
        elem[1] < 300
    ),
    cities
)

for elem in filtered:
    print(elem)
