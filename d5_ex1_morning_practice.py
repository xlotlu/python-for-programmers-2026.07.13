# Exercițiu
# Dat fiind template-ul de decorator
def mydeco(func):

    def _inner(*args, **kwargs):
        print("» sunt în decorator!")
        print("» execut funcția reală:")
        retval = func(*args, **kwargs)

        print("» ies din decorator!")
        return retval

    return _inner

# Scrieți un decorator
def timeit(func):
    pass
# ce printează timpul de execuție
# al funcției pe care o decorează.


from datetime import datetime
import time

def timeit(func):
    def _inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Timp de execuție: {end - start}")
        return result
    return _inner

@timeit
def sleepy(y):
    time.sleep(y)


# Exercițiu:
# scrieți un decorator
import sys

def logit(stream=sys.stderr):
    pass

# `stream` este un obiect care suportă metoda write.
# decoratorul va fi folosit astfel:
#@logit()
#def myfunc():
#    pass
#
# aceasta înseamnă că va funcționa astfel:
#myfunc = logit()(myfunc)

# sau:
# LOG_FILE = open('log.txt', 'a')
# @logit(LOG_FILE)
# def myfunc():
#    pass
#
# _intermed = logit(LOG_FILE)
# myfunc = _intermed(myfunc)

# până acum un decorator a fost:
def deco(func):
    def _inner():
        pass
    return _inner

# acum decoratorul este:
def deco(param):
    def _real_deco(func):
        def _inner(*args, **kwargs):
            pass
        return _inner
    return _real_deco


from datetime import datetime
from itertools import chain

AUDIT_TEMPLATE = "[{timestamp}] {module}.{function}({params}) --> {retval}\n"
def audit(stream=sys.stderr):
    def _audit_deco(func):
        def _inner(*args, **kwargs):
            now = datetime.now()

            params = [
                repr(v) for v in args
            ] + [
                f"{k}={repr(v)}"
                for k, v in kwargs.items()
            ]

            # sau, folosind chained generator expressions
            # (very nice but useless optimisation here)
            params = chain(
                (repr(v) for v in args),
                (f"{k}={repr(v)}" for k, v in kwargs.items())
            )

            retval = func(*args, *kwargs)

            stream.write(
                AUDIT_TEMPLATE.format(
                    timestamp=now.timestamp(),
                    module=func.__module__,
                    function=func.__qualname__,
                    params=", ".join(params),
                    retval=retval,
                )
            )
            stream.flush()

            return retval
        return _inner
    return _audit_deco


LOG_FILE = open('log.txt', 'a')
@audit(LOG_FILE)
def my_func(arg1, arg2, *args, encoding='utf-8', overwrite=False, **kwargs):
    return arg1 + arg2

my_func("bla", "și blu", "și etc")
my_func("blu", "ble", encoding="cp1252", something_else="wow!")

