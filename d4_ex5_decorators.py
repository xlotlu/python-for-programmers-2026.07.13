from functools import cache
from random import randint

def myfunc():
    return randint(1, 100)
# random
myfunc()
myfunc()

#decorated: not random
@cache
def myfunc():
    return randint(1, 100)
myfunc()
myfunc()

# un decorator este o funcție, care primește ca argument o funcție, și returnează o funcție

def myfunc():
    return randint(1, 100)
cache(myfunc)
decorated_func = cache(myfunc)
decorated_func()
decorated_func()

def myfunc():
    return randint(1, 100)
# in-place replacement
myfunc = cache(myfunc)
myfunc()
myfunc()

@cache # "syntactic sugar" pentru myfunc = cache(myfunc)
def myfunc():
    print("mă rulez!")
    return randint(1, 100)
myfunc()
myfunc()

# cu argumente
@cache
def myfunc(a, b):
    print("mă rulez!")
    return randint(a, b)
myfunc(1, 100)
myfunc(1, 100)
myfunc(1, 99)
myfunc(1, 99)
myfunc(2, 100)
myfunc(2, 100)

from functools import lru_cache # least-recently used cache

@lru_cache
def myfunc(a, b):
    print("mă rulez!")
    return randint(a, b)

@lru_cache(maxsize=3)
def myfunc(a, b):
    print("mă rulez!")
    return randint(a, b)
myfunc(1, 100)
myfunc(1, 100)
myfunc(2, 100)
myfunc(2, 100)
myfunc(3, 100)
myfunc(3, 100)
myfunc(4, 100)
myfunc(3, 100)
myfunc(2, 100)
# this is evicted
myfunc(1, 100)

# lru_cache has optional param
@lru_cache(maxsize=3)
def myfunc(a, b):
    print("mă rulez!")
    return randint(a, b)

@lru_cache
def myfunc(a, b):
    print("mă rulez!")
    return randint(a, b)

# so it works like this
lru_cache(myfunc)
# and like this
lru_cache(maxsize=3)(myfunc)

# like this
lru_cache()(myfunc)
# and like this
lru_cache(myfunc)


## scriem un decorator

# un decorator este o funcție, care primește ca argument o funcție, și returnează o funcție
def mydeco(func):

    def _inner():
        return "42: the meaning of life"

    return _inner
# hitchiker's guide to the galaxy
@mydeco
def myfunc():
    return "rezultat!"
myfunc()

def mydeco(func):

    def _inner():
        print("» sunt în decorator!")
        print("» execut funcția reală:")
        retval = func()

        print("» ies din decorator!")
        return retval

    return _inner

@mydeco
def myfunc():
    print("-- eu sunt funcția reală")
    return "rezultat!"

myfunc()

# dar cu argumente??
def mydeco(func):

    # este nevoie de un decorator cu aceeași semnătură
    def _inner(a, b):
        print("» sunt în decorator!")
        print("» execut funcția reală:")
        retval = func(a, b)

        print("» ies din decorator!")
        return retval

    return _inner

@mydeco
def myfunc(a, b):
    print("-- eu sunt funcția reală")
    return f"rezultat, cu args: {a}, {b}"

myfunc(1, 2)


# sau de un decorator care propagă toate argumentele

def mydeco(func):

    def _inner(*args):
        print("» sunt în decorator!")
        print("» execut funcția reală:")
        retval = func(*args)

        print("» ies din decorator!")
        return retval

    return _inner

@mydeco
def myfunc(a, b, c):
    print("-- eu sunt funcția reală")
    return f"rezultat, cu args: {a}, {b}, {c}"

myfunc(1, 2, 3)

# și toate kwargs

def mydeco(func):

    def _inner(*args, **kwargs):
        print("» sunt în decorator!")
        print("» execut funcția reală:")
        retval = func(*args, **kwargs)

        print("» ies din decorator!")
        return retval

    return _inner

@mydeco
def myfunc(a, b, c):
    print("-- eu sunt funcția reală")
    return f"rezultat, cu args: {a}, {b}, {c}"

myfunc(1, 2, 3)
