
from contextlib import ExitStack

paths = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:

    files = []

    for p in paths:
        f = stack.enter_context(open(p, "w"))
        files.append(f)
        print("Ouverture de", p)

    for f in files:
        f.write("Programmation\n")

    print("Ecriture terminée")

print("Tous les fichiers sont fermés")
