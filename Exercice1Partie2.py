
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def temp_file():

    path = Path("temp.txt")
    f = path.open("w")

    print("Ouverture du fichier")

    try:
        yield f

    finally:
        f.close()
        print("Fermeture du fichier")

        if path.exists():
            path.unlink()
            print("Suppression du fichier")


with temp_file() as f:
    f.write("Autre test\n")
    f.write("Test avec contextmanager\n")

print("Fin du programme")
