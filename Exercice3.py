
import csv
from datetime import datetime


class BatchProcessor:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fichier_csv = None
        self.journal = None

    def __enter__(self):

        try:
            
            self.fichier_csv = open(self.csv_file, "r", encoding="utf-8")

            
            self.journal = open("journal.log", "a", encoding="utf-8")

            
            self.journal.write(
                f"[{datetime.now()}] Début du traitement\n"
            )
            self.journal.flush()

            print("Fichiers ouverts avec succès.")

            return self

        except OSError as e:

            print("Erreur lors de l'ouverture des fichiers :", e)

            if self.fichier_csv is not None:
                self.fichier_csv.close()

            if self.journal is not None:
                self.journal.close()

            raise

    def traiter(self):

        try:
            lecteur = csv.reader(self.fichier_csv)

            for ligne in lecteur:

                if not ligne:
                    continue

                operation = ligne[0]

                print("Traitement de :", operation)

                self.journal.write(
                    f"[{datetime.now()}] Opération traitée : {operation}\n"
                )
                self.journal.flush()

        except (OSError, csv.Error) as e:

            self.journal.write(
                f"[{datetime.now()}] Erreur de traitement : {e}\n"
            )
            self.journal.flush()

            raise

    def __exit__(self, exc_type, exc_value, traceback):

        try:
            if exc_type:
                message = f"Erreur détectée : {exc_type.__name__} - {exc_value}"
                print(message)

                if self.journal is not None and not self.journal.closed:
                    self.journal.write(
                        f"[{datetime.now()}] {message}\n"
                    )

            else:
                print("Traitement terminé avec succès.")

            if self.journal is not None and not self.journal.closed:
                self.journal.write(
                    f"[{datetime.now()}] Fin du traitement\n"
                )

        except OSError as e:
            print("Erreur d'écriture dans le journal :", e)

        finally:
            
            if self.fichier_csv is not None and not self.fichier_csv.closed:
                self.fichier_csv.close()

            if self.journal is not None and not self.journal.closed:
                try:
                    self.journal.close()
                except OSError as e:
                    print("Erreur lors de la fermeture du journal :", e)

        return False



with BatchProcessor("operations.csv") as batch:
    batch.traiter()
