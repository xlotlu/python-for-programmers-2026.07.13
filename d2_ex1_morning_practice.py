# Creați un string cu string-ul "tralala" repetat de 7 ori
"tralala" * 7

# Obțineți partea întragă a împărțirii lui 17 la 4.
17 // 4

# Obțineți restul împărțirii lui 17 la 4.
17 % 4

# 8 la puterea a 3a?
8 ** 3

# ======== #

# Scrieți o funcție `cube(x)` ce calculează `x` la puterea a 3a.
def cube(x):
    return x ** 3

# Dat fiind variabila globală
M_TO_FT = 3.28084
# scrieți două funcții de conversie,
# `feet_to_meters(ft)` și `meters_to_feet(m)`.

def meters_to_feet(m):
    return m * M_TO_FT

def feet_to_meters(ft):
    return ft / M_TO_FT

# ======== #

# Dat fiind string-ul template
t = "Dear {name}, you just received €{amount} in your account {account}."
#   folosiți metoda .format() pentru a popula string-ul.
t.format(name="John", amount=10000000, account="RO12XXXX")

# ======== #

# Scrieți o funcție
def format_minutes(total_minutes):
    pass
# ce returnează un string de forma "ore:minute".
# Exemplu: 72 --> 1:12; 62 --> 1:02

def format_minutes(total_minutes):
    hours = total_minutes // 60;
    minutes = total_minutes % 60;

    return f"{hours}:{minutes:02d}"

# Scrieți o funcție
def get_greeting(hour):
    pass
# ce returnează unul din stringurile:
# între 5 și 10: "Bună dimineața"
# între 10 și 18: "Bună ziua"
# între 18 și 22: "Bună seara"
# între 22 și 5: "Noapte bună"

def get_greeting(hour):
    if hour < 0 or hour > 23:
        raise ValueError("Oră invalidă")

    if 5 <= hour < 10:
        return "Buna dimineata"
    elif 10 <= hour < 18:
        return "Buna ziua"
    elif 18 <= hour < 22:
        return "Buna seara"
    else:
        return "Noapte buna"

# Apoi scrieți o funcție
def get_current_greeting():
    pass
# ce află care este ora curentă și o apelează pe cea de mai sus
# pentru a returna string-ul potrivit pentru momentul actual.
#
# hints:
# from datetime import datetime
# datetime.now() # <-- returnează un obiect
# acest obiect are atributul hour

from datetime import datetime

def get_current_greeting():
    now = datetime.now()
    return get_greeting(now.hour)


# Scrieți o funcție `is_leap_year(year)` ce returnează bool.
#
# un an bisect:
# a) este divizibil cu 4, dar
# b) nu este divizibil cu 100,
# c) decât dacă este totuși divizibil cu 400.
#
# testați funcția pe anii 2020, 2021, 2022, 2000, 1900

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

for y in 2020, 2021, 2022, 2000, 1900:
    print(y, is_leap_year(y))


# ======== #

# printați toate numerele întregi de la 100 la 124
# folosind `for` și `range()`.
for number in range(100, 125):
    print(number)

# printați toate numerele întregi de la 100 la 124
# folosind `while`.
number = 100
while number < 125:
    print(number)
    number += 1

# Scrieți o funcție
def find_appearances(lst, s):
    pass
# ce, primind o listă, detectează numărul de apariții
# al substringului `s` în elementele lui `lst`.
# Exemplu:
#find_appearances(["ala", "bala", "porto", "cala", "tralalala"], "ala") == 5

def find_appearances(lst, s):
    total = 0
    for elem in lst:
        total += elem.count(s)
    return total

# Scrieți o funcție
def validate_password(pwd):
    pass
# ce validează parola `pwd` și returnează True / False
# pe baza următoarelor criterii:
# - are cel puțin 8 caractere
# - conține cel puțin o literă mare
# - conține cel puțin o literă mică
# - conține cel puțin un număr
#
# folosiți metodele str .isupper() .islower() .isdigit()

def validate_password(pwd):
    if len(pwd) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in pwd:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        # optimisation, we return inside the for
        # if already valid
        if has_upper and has_lower and has_digit:
            return True

    return False


# Scrieți o funcție
def timer(s):
    pass
# ce primește ca parametru un număr de secunde
# și face print secundelor rămase până la 0.
from time import sleep

def timer(s):
    # for x in range(s, 0, -1): ...
    while s >= 0:
        print(f"Secunde ramase: {s}")
        sleep(1)
        s -= 1

# [opțional] Scriem un timer care printează
# doar din când în când (la fiecare `skip` secunde):
def skipping_timer(s, skip=5):
    pass

def skipping_timer(s, skip=5):
    initial = s
    while s >= 0:
        if (initial - s) % skip == 0:
            print(f"Secunde ramase: {s}")

        sleep(.1)
        s -= 1

# v.2. sleep cu skip
def skipping_timer(s, skip=5):
    initial = s
    while s >= 0:
        print(f"Secunde ramase: {s}")

        sleep(min(s, skip))
        s -= skip

# v.3. cu for și range
def skipping_timer(s, skip=5):
    for interval in range(s, 0, -skip):
        print(f"Secunde ramase: {interval}")
        if interval < skip:
            sleep(interval)
        else:
            sleep(skip)
    print('=== Done ===')

# v.3.1 același lucru, printat pe o singură linie
def skipping_timer(s, skip=5):
    for interval in range(s, 0, -skip):
        print(f"\rSecunde ramase: {interval}", end="")
        if interval < skip:
            sleep(interval)
        else:
            sleep(skip)
    print('\n=== Done ===')
