# positional arguments
def myfunc(a, b):
    pass
myfunc(1, 2)

# positional + keyword arguments
def myfunc(a, b, c="default"):
    pass
myfunc(1, 2)
# all can be passed as positional
myfunc(1, 2, 3)
# or all can be passed as keyword
myfunc(c=3, a=1, b=2)

# catch-all positional (argument packing)
def myfunc(a, b, *args):
    print("» a", a)
    print("» b", b)
    print("» args", args)
myfunc(1, 2)
myfunc(1, 2, 3)
myfunc(1, 2, 3, 4, 5, 'etc.')

# catch-all positional + keyword
def myfunc(a, b, *args, kwarg1="default 1", kwarg2="default 2"):
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)
myfunc(1, 2, 3, 4)

# catch-all positional + catch-all keyword
def myfunc(a, b, *args, kwarg1="default 1", kwarg2="default 2", **kwargs):
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)
    print("» kwargs", kwargs)
myfunc(1, 2, 3, 4)
myfunc(1, 2, 3, 4, kwarg1="n-o-t default", kwargs_something="wow", kwarg_something_else="aha!")

# iterable unpacking ("sequence unpacking")
a, b, c = range(3)

# argument unpacking
lst = ["ala", "bala", "porto", "cala"]
print(*lst, sep=" ! ")
# is perfectly equivalent to
print("ala", "bala", "porto", "cala", sep=" ! ")

def myfunc(a, b, *args, kwarg1="default 1", kwarg2="default 2", **kwargs):
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)
    print("» kwargs", kwargs)
# works with any iterable
myfunc(*range(10)) # echivalent cu: myfunc(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# unpacking keyword args
d = {
    'kwarg2': "o valoare pentru kwarg 2",
    'alt_kwarg': "o valoare pentru altul",
    "și_tot_așa": "etc.....",
}
myfunc(*range(3), **d)
# echivalent cu
myfunc(*range(3), kwarg2='...2', alt_kwarg='...alt', și_tot_așa='...etc')

# also works with non-identifier arg names
d = {
    'kwarg2': "o valoare pentru kwarg 2",
    'alt kwarg': "o valoare pentru altul",
    "și tot așa": "etc.....",
}
myfunc(*range(3), **d)


# function definition: * and /

def myfunc(a, b, kw1="cu default"):
    pass
# this works (all args passed as positional)
myfunc(1, 2, 3)

# this doesn't
def myfunc(a, b, *, kw1="cu default"):
    pass
myfunc(1, 2, 3)

def myfunc(a, b, *, kw1="cu default"): # după * nu sunt permise poziționale
    pass
# must do this
myfunc(1, 2, kw1=3)

def myfunc(a, b, kw1="cu default"):
    pass
# this works (all arguments passed as keyword)
myfunc(a=1, b=2, kw1=3)

def myfunc(a, b, /, kw1="cu default"):
    pass
myfunc(1, 2, 3) # works
myfunc(1, 2, kw1=3) # works
myfunc(a=1, b=2, kw1=3) # not works
def myfunc(a, b, /, kw1="cu default"): # obligă argumentele poziționale să fie pasate doar ca poziționale
    pass

# exemplu din stdlib: semnătura lui `sorted()` este
# sorted(iterable, /, *, key=None, reverse=False)
myiter = ["tra", "la", "la"]
sorted(iterable=myiter) # fails
sorted(myiter) # ok
sorted(myiter, lambda x: x) # fails
sorted(myiter, key=lambda x: x) # ok
