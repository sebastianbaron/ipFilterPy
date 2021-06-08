
def inputreplace(r):
    r = r.replace("\n", "")
    r = r.replace("\t", "")
    r = r.replace(", ", "")
    r = r.split(",")
    return r

