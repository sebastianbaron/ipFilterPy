import os

from .inputReplace import inputreplace


def listchecker(a, b):
    curatednewlist = inputreplace(str(a))
    #print(curatednewlist)
    arraytoappend = []
    for i in curatednewlist:
        if i not in b:
            arraytoappend.append(i)
            print(" " + i + " is NOT OK")

    if len(arraytoappend) > 0:
        print("\n Ips a configurar : ")
        for i in arraytoappend:
            print(" " + i)

    return arraytoappend





