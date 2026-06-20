import os

def getContent(file):
    content = open(file, "r").read()
    return content

def appendTo(file, text):
    open(file, "a").write(text)

def wipeAndWrite(file, text):
    open(file, "w").write(text)

def isThere(file):
    return os.path.exists(file)