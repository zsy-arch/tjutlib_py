import sys

if len(sys.argv) <= 1:
    print("No arguments!")
    exit(-1)

name = sys.argv[1]
number = sys.argv[2]

with open("empty.html", "r+", encoding='utf-8') as file:
    file_content = file.read()
    fc = file_content.replace("$NAME$", name)
    fc = fc.replace("$NUMBER$", number)
    print(fc)
