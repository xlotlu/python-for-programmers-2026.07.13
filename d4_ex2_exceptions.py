# try trebuie să fie însoțit de (cel puțin un) except
try:
    1 / 0
except:
    print("catch all")

# sau de finally
try:
    1 / 0
finally:
    print("la final...")


# poate fi completat de else
try:
    1 / 0
except:
    print("o crăpat")
else:
    print("a mers try-ul")


# varianta cu toate patru
try:
    1 + 0
except:
    print("o crăpat")
else:
    print("a mers try-ul")
finally:
    print("și eu, aici tot timpul!")

try:
    1 / 0
except:
    print("o crăpat")
else:
    print("a mers try-ul")
finally:
    print("și eu, aici tot timpul!")


# pot exista mai multe except-uri
# și excepția poate fi capturată
try:
    1 / 0
    #d[lst[1]]
    int("bla")
except ZeroDivisionError:
    print("cauți infinitul?")
except (IndexError, KeyError):
    print("a-ha!")
except Exception as e:
    print("catch-all")
    print("» exc. a fost:", type(e), e)
    raise e


# varianta cu de toate
try:
    # statements
    pass
except IndexError:
    # o crăpat la listă
    pass
except KeyError:
    # o crăpat la dicționar
    pass
except Exception as e:
    # o crăpat undeva unde nu ne așteptam,
    # hai (spre exemplu) să logăm excepția
    pass
else:
    # totul a fost în regulă
    pass
finally:
    # indiferent ce, mă rulez
    pass
