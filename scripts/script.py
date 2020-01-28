# read the file
# test.txt -> obfuscated file
# dump.txt -> cleaned file
file = open("test.txt", "r")
dump = open("dump.txt", "w")

for line in file:
    if("Rem" not in line):
        dump.write(line)
