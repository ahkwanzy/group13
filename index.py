import sys
if len(sys.argv)>1:
    filename = sys.argv[1]
else:
    print "Your input is invalid!" #invalid input due to arguments
    exit()

def openFile(filename):
    usefile = open(filename, "r+")
    fileContent = usefile.read()
    usefile.close()
    print fileContent

openFile(filename)