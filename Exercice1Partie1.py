
from pathlib import Path

class TempFileWriter:

    def __enter__(self):
        self.filepath = Path("temp.txt")
        self.f = self.filepath.open("w")
        print("Ouverture du fichier")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print("Fermeture du fichier")

        if self.filepath.exists():
            self.filepath.unlink()
            print("Suppression du fichier")

        return False


with TempFileWriter() as f:
    f.write("Contenu temporaire\n")
    f.write("Deuxième ligne\n")

print("Fin du programme")
