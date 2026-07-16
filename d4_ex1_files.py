import os

# current working directory:
print("»", os.getcwd())

# relevant pentru
# - căile de import
# - open() de fișiere (relative paths)

# pentru a îl schimba:
#os.chdir("/my/path")

# atenție la căile de Windows,
# vrem să escape:
path = "C:\\Users\\MyName\\Desktop\\my-file.txt"
# sau, mai simplu, cu raw string:
path = r"C:\Users\MyName\Desktop\my-file.txt"


# în privința lucrării cu path-uri:
BASE_DIR = '/my/dir'

# opțiunea 1, old school:
from os import path
path.join(BASE_DIR, "subdir", "file.txt")

# opțiunea 2, modern, pythonic:
from pathlib import Path
Path(BASE_DIR) / "subdir" / "file.txt"


### chiar cu fișiere acum:

f = open("my-file.txt")

# în general nu vom lucra cu .read()
print(f.read()) # citește tot

# dacă aveți nevoie să citiți din nou de la început:
f.seek(0)
# dar... nu cumva e un anti-pattern?

# fișierul este iterabil!
for line in f:
    print(line)

f.seek(0)
# dacă vrem să normalizăm liniile să fie fără newline:
for line in f:
    print(line.removesuffix("\n"))

###    I M P O R T A N T ! ! !    ###
open(path, encoding="utf-8")

# nu uitați encoding-ul, și la read și la write
# (în cazul în care vreți interoperabilitate)
# (și la fel, în cazul în care aveți diacritice)


# ca să scriem:
f = open("file.txt", "w")
f.write("content\n")
f.write("another content")

# și la final....
f.close() # (doar că nu vom face asta)

# moduri
'w' # trunchează dacă există, altfel creează
'x' # doar creează, refuză să opereze pe ceva existent
'a' # append -- cursorul este deja la final


# Pe vremuri când eram eu tânăr măi tataie...
# făceam așa:
fp = open("file.txt", 'w')
try:
    fp.write("ceva content")
    1 / 0
finally:
    fp.close()

# Acum facem așa:
import datetime
with open("file.txt", 'w', encoding='utf-8') as fp:
    fp.write(f"ceva content -- {datetime.now()}")
    1 / 0


# Scrieți o funcție ce copiază un fișier

def cp(sourcepath, targetpath, overwrite=False, chunk=8192):
    if overwrite:
        mode = 'wb'
    else:
        mode = 'xb'

    # echivalent cu

    mode = 'wb' if overwrite else 'xb'

    with open(sourcepath, 'rb') as f_in, \
         open(targetpath, mode) as f_out:

        while content := f_in.read(chunk):
            f_out.write(content)

