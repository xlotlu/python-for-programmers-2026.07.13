print("Hello World")

# Exercițiu:
# cereți utilizatorului numele său
# folosind funcția input,
#
# apoi salutați-l frumos,
# cu un salut de forma "Salut <nume>"

#name = input("Numele tău? ")
#print("Salut " + name + "!")


# Exercițiu:
# age verification:
# cereți utilizatorului vârsta sa
#
# Dacă este mai mare sau egal cu 18 ani
# print "ești acceptat",
# altfel print "ești prea tânăr".

# age = input("Vârsta? ")
# # input returnează string
# age = int(age)

# if age < 18:
#     # indentat sub-blocul
#     print("ești prea tânăr")
# else:
#     print("ești acceptat")


# Ce facem dacă input-ul este număr invalid?
# TODO: învâțăm exception handling
#
# 1. îi zicem utilizatorului să bage input corect
# 2. facem din nou prompt

# Exercițiul:
# promptați utilizatorul la nesfârșit
# până când face input unui număr valid

while True:
    age = input("Vârsta? ")

    if age.isdecimal():
        age = int(age)
        break

    else:
        print("Mesaj de eroare")

if age < 18:
    # indentat sub-blocul
    print("ești prea tânăr")
else:
    print("ești acceptat")

# v.2
while True:
    age = input("Vârsta? ")

    if not age.isdecimal():
        print("Mesaj de eroare")
        continue

    else:
        age = int(age)
        break

if age < 18:
    # indentat sub-blocul
    print("ești prea tânăr")
else:
    print("ești acceptat")


# v.2.1
while True:
    age = input("Vârsta? ")

    if not age.isdecimal():
        print("Mesaj de eroare")
        continue

    age = int(age)
    break

if age < 18:
    # indentat sub-blocul
    print("ești prea tânăr")
else:
    print("ești acceptat")


# v.3.
age = input("Vârsta? ")

while not age.isdecimal():
    print("error")
    age = input("Vârsta? ")

age = int(age)
# etc.