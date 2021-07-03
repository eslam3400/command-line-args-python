from sys import argv

if len(argv) >= 1: print(f"hello ,{argv[1]}")
else: print("no arguments")

for arg in argv: print(arg)