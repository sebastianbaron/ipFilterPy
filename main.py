import os
from functions.listChecker import listchecker

# ip input from 'newIp.txt'

os.getcwd()
os.chdir('src')

with open("oldIp.txt") as ol:
    oldlist = ol.read()
    oldlist = oldlist.split(",")
    # print(type(oldList))
    # print(oldList)

with open("newIp.txt") as nl:
    newlist = nl.read()
    # print(newList)

arraytoappend = listchecker(newlist, oldlist)


with open("oldIp.txt", "a") as ol:
    for i in arraytoappend:
        ol.write(i + ",")


input("\n Press ENTER to exit")





