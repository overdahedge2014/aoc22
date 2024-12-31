

def op(filename):
    fd = open(filename)
    return fd.read()

def op(filename, splitter):
    fd = open(filename)
    return fd.read().split(splitter)