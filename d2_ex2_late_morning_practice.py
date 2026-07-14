# Dată fiind lista
l = [1, 2, 3, 4, 5]
# calculați suma pătratelor elementelor din listă
total = 0
for num in l:
    total += num ** 2

# Dată fiind lista de tuple de forma (nume, vârstă)
candidates = [
    ('Mara', 28),
    ('George', 16),
    ('Dragoș', 42),
    ('Ana', 74),
    ('Mircea', 31),
    ('Carmen', 17),
    ('Andreea', 38),
    ('Vasi', 61),
]
# creați două liste noi `accepted` și `rejected`
# astfel încât persoanele cu vârsta între 18 și 60 de ani
# sunt accepted, iar restul rejected.

accepted = []
rejected = []

for elem in candidates:
    if 18 <= elem[1] < 60:
        accepted.append(elem)
    else:
        rejected.append(elem)

# Repetați exercițiul de mai sus
# consumând lista inițială în timp ce iterați
# (la sfârșit lista rămâne goală)
# 
# hint: folosiți metoda .pop() a listei.

accepted = []
rejected = []

while candidates:
    elem = candidates.pop()

    if 18 <= elem[1] < 60:
        accepted.append(elem)
    else:
        rejected.append(elem)

# rezultat ok, dar listele sunt invers.

# Întrebare: Dacă voiam să păstrăm ordinea inițială?
#
# Răspuns 1: folosim .pop(0)
#      implicație: se re-indexează toată lista de len(list) ori.
#
# Răspuns 2: facem în prealabil .reverse()
#      implicație: se re-indexează lista o singură dată.


# ===== #

# Dată fiind structura de date conținând o listă de
# [name, age, hobbies]
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# a) îmbătrâniți-o pe Jane cu 1 an.
friends[0][1] += 1

# b) Adăugați hobby-urilor Annei "reading" și "cooking"
friends[2][2].extend(["reading", "cooking"])

# c) Ștergeți-i lui Mike ultimul hobby
del friends[1][2][-1]

# d) Adăugați un prieten nou
["Ginger", 22, ["reading", "cooking", "hiking"]]

friends.append(["Ginger", 22, ["reading", "cooking", "hiking"]])

# [opțional] Și pentru Cosmin (și cine mai vrea):
# Sortați lista friends după vârstă
# știind că există metoda .sort()
# care primește parametru opțional key=o funcție
friends.sort(key=lambda elem: elem[1])

# Scrieți o funcție
def get_friend_by_name(friends, name):
    pass
# ce primind o structură de date ca mai sus
# returnează elementul cu numele dat
def get_friend_by_name(friends, name):
    for friend in friends:
        if friend[0] == name:
            return friend

# Scrieți o funcție
def find_friends_by_hobby(friends, hobby):
    pass
# ce returnează o listă cu elementele din `friends`
# care au respectivul `hobby`

def find_friends_by_hobby(friends, hobby):
    result = []

    for friend in friends:
        if hobby in friend[2]:
            result.append(friend)

    return result

#print(find_friends_by_hobby(friends, 'reading'))

# alternativ:
def find_friends_by_hobby(friends, hobby):
    return filter(lambda elem: hobby in elem[2], friends)

# Scrieți o funcție
def find_friends_by_age(friends, min_age, max_age=None):
    pass
# ce returnează lista prietenilor cu vârstă mai mare
# sau egal cu `min_age` și, dacă este specificat,
# cu vârstă mai mică decât `max_age`.

def find_friends_by_age(friends, min_age, max_age=None):
    result = []

    for friend in friends:
        age = friend[1]
        if age >= min_age and (
            max_age is None or age < max_age
        ):
            result.append(friend)

    return result

# Scop final:
# Găsiți toți prietenii cu vărstă între 18 și 60 de ani
# și cu hobby hiking
find_friends_by_age(
    find_friends_by_hobby(friends, "hiking"),
    18, 60
)

# Adăugați tuturor prietenilor cu vârsta peste 30 de ani
# hobby-ul "knitting"
for f in find_friends_by_age(friends, 30):
    f[2].append("knitting")
