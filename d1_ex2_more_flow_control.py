# Task:
# scriem o funcție ce se asigură
# că primește input număr întreg
# de la utilizator
# și returnează numărul

def prompt_int(prompt=''):
    # aici trebuie să ne asigurăm că num
    # este număr întreg
    while True:
        num = input(prompt)
        if num.isdecimal():
            return int(num)
        
        print("Eroare. Introdu număr întreg.")

#print("ai introdus", prompt_int())

# Exercițiu:
# Cereți utilizatorului vârsta sa.
# - dacă este < 18 ani: "ești prea tânăr"
# - dacă este între 18 și 60 de ani: "ești acceptat"
# - dacă este > 60 de ani: "ești prea în vârstă"

def check_age(age):
    if age >= 18 and age <= 60:
        print('Esti adult!')
    elif age > 60:
        print('Esti prea batran!')
    elif age < 18:
        print('Esti prea tanar!')

def _exercitiu():
    age = prompt_int("Care este vârsta ta? ")
    check_age(age)

#_exercitiu()


# Exercițiu:
# Cereți utilizatorului
# vârsta sa și vârsta prietenului său.
#
# apoi faceți print cu diferența de vârstă.

def _exercitiu():
    varsta1 = prompt_int("Da-mi varsta ta ")
    varsta2 = prompt_int("Da-mi varsta prietenului tau ")

    print("Diferenta intre varste este", abs(varsta2 - varsta1))

#_exercitiu()

# Exercițiu:
# Cereți vârsta utilizatorului și a unui prieten,
# apoi faceți print cu unul din următoarele string-uri, după caz:
#
# "Ești mai în vârstă decât prietenul tău cu <diff> ani."
# "Prietenul tău este mai în vârstă cu <diff> ani."
# "Aveți aceeași vârstă."

def verify_age_diference(age1, age2):
    diff = abs(age1 - age2)

    if age1 > age2:
        print(f"Primul user este mai batran cu {diff} ani.")
    elif age1 < age2:
        print(f"Al doilea user este mai batran cu {diff} ani.")
    else:
        print("Ambii useri au aceeasi varsta.")

def _exercitiu():
    varsta1 = prompt_int("Da-mi varsta ta ")
    varsta2 = prompt_int("Da-mi varsta prietenului tau ")

    verify_age_diference(varsta1, varsta2)
#_exercitiu()

# alternativ:
TEMPLATE = "Vârsta {cui} este mai mare cu {diff} ani."

def verify_age_diference(age1, age2):
    diff = abs(age1 - age2)

    if age1 > age2:
        user = "ta"
    else:
        user = "celuilalt"

    print(TEMPLATE.format(cui=user, diff=diff))

_exercitiu()