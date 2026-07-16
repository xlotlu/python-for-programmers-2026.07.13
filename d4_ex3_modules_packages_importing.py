# ne facem primul modul:
# creăm un fișier:
# "mymodule.py"

import mymodule

mymodule.VERSION
mymodule.func()


# chestii relevante
import sys
sys.path
sys.modules

# atenție!
# modulele sunt cache-uite.
# atâta timp cât există în `sys.modules`
# la orice `import` ulterior modulele este încărcat din cache.

# ulterior = orice zonă a aplicației tale
#          = oricând, și peste un an, dacă nu s-a oprit aplicația
#          = oricum, chiar dacă ai modificat fișierul

# implicație fundamentală:
# top-level code al acelui modul
#    !!! se rulează o singură dată per lifetime-ul aplicației !!!


# =====

# Teoria, toată:

# prima formă
import mymodule
import mymodule as modalias

import mymodule, os, sys # don't do this

# a doua formă:
from mymodule import myfunc
from mymodule import myfunc, VERSION
from mymodule import myfunc as myf
from mymodule import (
    myfunc as myf,
    VERSION as VER,
)
from mymodule import * # somehwat frowned upon
