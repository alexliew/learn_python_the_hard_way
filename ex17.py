from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print("Copying from {!s} to {!s}".format(from_file, to_file))

# in_file = open(from_file)
# indata = in_file.read()
# The following works because the file will be closed once there are no more references to it. This is a feature of CPython's reference counting garbage collection mechanism however and is not a feature of the language.
indata = open(from_file).read()

# print("The input file is {:d} bytes long".format(len(indata)))

# print("Does the output file exist? {!r}".format(exists(to_file)))
input("Ready, hit RETURN to continue, CTRL-C to abort.")

out_file = open(to_file, 'w')
out_file.write(indata)

# print("Alright, all done.")

out_file.close()
in_file.close()
