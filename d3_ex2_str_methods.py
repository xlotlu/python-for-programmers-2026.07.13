s = "Este o dimineață minunată de mers la plajă."

### most useful

s.replace(" ", "\n")

s.count('substr')

# fac exact același lucru, doar că...
s.index('minunată')
s.find('minunată')

# ... .index() raises ValueError
#     .find()  returns -1
#
# Notă: .index() este varianta pythonică.

if s.find('substr') != -1:
    print("we have a match")
else:
    print("no match")

try:
    s.index('substr')
    print("we have a match")
except ValueError:
    print("no match")

try:
    s.index('substr')
except ValueError:
    print("no match")
else:
    print("we have a match")


s.split() # returnează listă.
# fără argument splitează pe _orice grupare de_ whitespace

# cu argument doar după acel substr:
user, domain = "my.name@domain.com".split("@")

# cu maxsplit:
directory, filename = "/path/to/myfile.txt".rsplit('/', 1)


# inversul lui split, join
" | ".join(["Column 1", "Column 2", "Column 3"])


s.splitlines()
# este ce vrem când splităm după rânduri
# un input mare multi-line
# (ex: conținutul unui fișier text)


### string fromatting

"{} are {} ani".format("Gigel", 17)
"{name} are {age} ani".format(name="Gigel", age=17)

"{name:=^22} are {age:04d} ani".format(name="Gigel", age=17)

"{name:=^22} are {age:04d} ani".format_map({
    "name": "Gigel",
    "age": 17
})


### utile pentru curățare
# s.strip() / s.lstrip() / s.rstrip()

# default, curăță orice whitespace:
" Gigel Popescu  \t \n".strip()

# cu argument, curăță acele caractere
"xybla blayyyyyxxxx".strip("xy")

# și prietenii, lstrip / rstrip
"00012340".lstrip("0")

### utile, uneori, manipulare de string
# s.removesuffix()
# s.removeprefix()
# curăță _specific_ acel substr dacă este prefix / sufix
js_line1 = "console.log('something');"
js_line2 = "console.log('something')"
js_line1.removesuffix(';') == js_line2.removesuffix(';')

### utile, uneori
s.startswith("substr")
s.endswith("substr")

### utile, rareori, manipulare de lower / upper case
s.lower()
s.upper()

s.capitalize()
s.title()

s.casefold() # de folosit la comparare de string-uri
             # pentru normalizare case-insensitive.
             #
             # (face ce trebuie întotdeauna,
             # spre deosebire de .lower()!)

### util rareori sau deloc
### (dar când e util, este)

table = str.maketrans("mn", "xy")
s.translate(table)
# echivalent cu:
s.replace("m", "x").replace("n", "y")


### not really, pentru output în consolă
# .rjust()
# .ljust()
# .center()
t = "un text"
t.center(20)
t.ljust(20, ' ')
t.ljust(20, '=')
t.rjust(20, '=')


### ... ok but why?
# .partition()
# .zfill()
# .expandtabs()

### probabil nu veți folosi acestea direct vreodată
bytes_obj = s.encode("utf-8")
back_to_str = bytes_obj.decode("utf-8")
