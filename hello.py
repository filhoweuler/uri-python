def _f(_a, _b):
    """ Returns a, multiplied b times """
    return _a ** _b

def _p(string, times):
    """ Prints the string variable times times """
    for i in range(times):
        print(string)

NAME = "Weuler"
_p(NAME, 2)
_p("Testolando", 10)
print(type(NAME))
print(_f(2, 8))
