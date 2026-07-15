# dicționare, use-cases

# colecție de valori, cu cheie "id"-ul lor
ages = {
    "Jane": 20,
    "Mike": 17,
}

# este de fapt la fel ca sus
rows = {
    1: ["Jane", 20, ["reading", "hiking", "biking"]],
    99: ["Mike", 17, ["hiking", "fishing"]],
}

# object-like
friend = {
    "name": "Jane",
    "age": 20,
    "hobbies": ["reading", "hiking", "biking"],
}


# din nou, colecție:
cities = {
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    # ...
}

# vs. colecție de "obiecte"
cities = [
    {
        'name': 'Cluj-Napoca',
        'distance': 450,
        'altitude': 320,
    },
    {
        'name': 'Timișoara',
        'distance': 550,
        'altitude': 180,
    },
]

# vs. colecție de "obiecte" accesibile după "id"

cities = {
    'Cluj-Napoca': {
        'name': 'Cluj-Napoca',
        'distance': 450,
        'altitude': 320,
    },
    'Timișoara': {
        'name': 'Timișoara',
        'distance': 550,
        'altitude': 180,
    },
}


# dată fiind tupla
friend = ("Dan", 34, ["painting", "reading"])

# transformați-l într-un dicționar cu cheile
# name, age, hobbies

{
    "name": friend[0],
    "age": friend[1],
    "hobbies": friend[2],
}

# sau, același lucru:
name, age, hobbies = friend
{
    "name": name,
    "age": age,
    "hobbies": hobbies,
}

# dată fiind colecția de tuple de forma (name, distance):
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

# creați un dicționar de forma
# {
#     name1: distance1,
#     name2: distance2,
#     ...
# }
#
# adică
{
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    # ...
}

# notă: este pattern de acumulare
#       doar că acumulăm într-un dicționar

out = {}
for name, distance in cities:
    out[name] = distance

# sau, cu dictionary comprehension
{
    name: distance
    for name, distance in cities
}

# sau... știind că poate fi inițializat
# dintr-un iterabil ale cărui elemente
# sunt la rândul lor iterabile cu 2 elemente....
dct = dict(cities)

# modalități de a itera dicționarul:

# iterare direct în dicționar, după chei:
for elem in dct:
    print(elem)

# același lucru, doar că suntem expliciți:
for elem in dct.keys():
    print(elem)

# iterare doar în valori:
for elem in dct.values():
    print(elem)

# iterare pe tuplele (key, value):
for elem in dct.items():
    print(elem)

# la fel, dar mai frumos
for key, value in dct.items():
    print(key, value, sep=': ')


# Exercițiu:
# dat fiind raportul primit ca string cu acest format:
s = """-----------------------------------
| Name       | Age | City         |
-----------------------------------
| Gigel      |  20 | Copenhaga    |
| Andrei     |  42 | București    |
| Georgiana  |  20 | Timișoara    |
| Andreea    |  20 | Constanța    |
| Carmencita |  20 | Satu Mare    |
| George     |  20 | Sfântu Gheor |
-----------------------------------"""

# scrieți o funcție parse_report(txt)
# ce returnează o listă de dicționare de forma:
# [
#     {'Name': 'Gigel', 'Age': 20, 'City': 'Copenhaga'},
#     {'Name': 'Andrei', 'Age': 42, 'City': 'București'},
#     ...
# ]
# în care cheile sunt numele coloanelor din header
# iar valorile cele din corpul tabelului.


def parse_row(line):
    return [
        col.strip()
        for col in line.split('|')[1:-1]
    ]

def parse_report(txt):
    result = []

    lines = txt.splitlines()

    columns = parse_row(lines[1])

    for line in lines[3:-1]:
        row = parse_row(line)

        # v1: construim dict manual
        data = {}

        for idx, column in enumerate(columns):
            value = row[idx]
            data[column] = value

        # v2: dict comprehension:
        data = {
            column: row[idx]
            for idx, column in enumerate(columns)
        }

        # v3: foarte Pythonic:

        data = dict(zip(columns, row))


        result.append(data)

    return result


# scurtăm maxim:
def parse_report(txt):
    lines = txt.splitlines()
    columns = parse_row(lines[1])

    return [
        dict(zip(columns, parse_row(line)))
        for line in lines[3:-1]
    ]

# dat fiind dicționarul
cities = {
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    'Iași': 400,
    'Constanța': 225,
    'Craiova': 230,
    'Brașov': 180,
    'Galați': 250,
    'Ploiești': 60,
    'Oradea': 600,
    'Brăila': 200,
    'Arad': 580,
    'Sibiu': 275,
    'Bacău': 300,
    'Târgu Mureș': 330,
    'Baia Mare': 600,
    'Buzău': 110,
    'Satu Mare': 640,
    'Suceava': 450,
}

# creați 2 dicționare noi:
# close_cities cu orașele <= 200 km, și
# far_cities cu orașele > 100km
#
# faceți aceasta consumând dicționarul inițial
# (la sfârșit rămâne gol).

close_cities = {}
far_cities = {}

while cities:
    name, distance = cities.popitem()

    if distance <= 200:
        close_cities[name] = distance
    else:
        far_cities[name] = distance
