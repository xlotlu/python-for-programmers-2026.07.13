def myiter():
    print("» intru în funcție")
    yield 1
    print("» sunt tot în funcție")
    yield 2
    print("» ies din funcție")

# for elem in myiter():
#     print(elem)

# un iterator care primește un iterabil cu elementele numere
# și dă pătratele acestora

def squares(numbers):
    out = []
    for n in numbers:
        out.append(n ** 2)
    return out

# for elem in squares(range(10)):
#     print(elem)

# varianta generator function

def squares(numbers):
    for n in numbers:
        yield n ** 2

# for elem in squares(range(10)):
#     print(elem)

# pentru situații simple,
# putem face comprehension
# ("generator expression")

def squares(numbers):
    return (
        n ** 2
        for n in numbers
    )

# for elem in squares(range(10)):
#     print(elem)


# Exercițiu:
# dat fiind datasetul "temperatures.csv"
# agregați media valorilor orare

import csv
from datetime import time
from time import sleep
from collections import defaultdict

def load_temps_csv(fname):
    "yields tuples of the form (datetime.time, float)"
    with open(fname) as f:
        for timestamp, value in csv.reader(f):
            #time(*[int(x) for x in timestamp.split(':')])
            #time.strptime(timestamp, '%H:%M:%S')
            yield time.fromisoformat(timestamp), float(value)

            # let's pretend slow network
            sleep(.0001)


def aggreggate_temps(iter):
    sums = defaultdict(list)
    for timestamp, value in iter:
        sums[timestamp.hour].append(value)

    return {
        hour: sum(totals) / len(totals)
        for hour, totals in sums.items()
    }

# cel de mai sus...
# 1) umple memoria
# 2) ia timp până se procesează tot

# strategia 2:
# când se schimbă ora calculăm average-ul pentru ora trecută
# și trecem mai departe

def aggreggate_temps(iter):
    hourly_sum = 0
    hourly_count = 0

    prev_tstamp = None

    for timestamp, value in iter:
        # ne normalizăm timestamp-ul la rezoluția de agregare
        # necesară (în acest caz, orară)
        timestamp = timestamp.replace(minute=0, second=0)
        # strategie dacă voiam să facem agregare la minut:
        #timestamp = timestamp.replace(second=0)

        if timestamp != prev_tstamp and prev_tstamp is not None:
            # do some hour-changing logic

            yield timestamp, hourly_sum / hourly_count

            hourly_sum = 0
            hourly_count = 0

        hourly_sum += value
        hourly_count += 1

        prev_tstamp = timestamp

    yield timestamp, hourly_sum / hourly_count


for elem in aggreggate_temps(load_temps_csv('data/temperatures.csv')):
     print(elem)
