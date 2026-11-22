
from datetime import datetime
from contextlib import ExitStack

class ConnectionManager:

    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(f"Connexion à {self.service_name} établie.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Déconnexion de {self.service_name}.")

        if exc_type:
            print(f"Erreur détectée : {exc_type.__name__} — {exc_value}")

        return False


with ExitStack() as stack:

    log = stack.enter_context(open("log.txt", "a"))

    conn = stack.enter_context(ConnectionManager("Base Y"))

    log.write(f"[{datetime.now()}] Connexion à {conn.service_name}\n")

    print("Début du traitement...")

    raise RuntimeError("Erreur de traitement")

print("Fin du programme")
