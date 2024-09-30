# Version mit globaler Variable
counter = 0


def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")
    return counter


# Ihr Ziel ist es, diesen Code zu refaktorieren,
# um die globale Variable durch ein Closure (create_counter) zu ersetzen.
def create_counter():
    # TODO: Implementieren Sie hier die Funktion create_counter
    ...


if __name__ == "__main__":
    # Auch mit dem Closure soll der Aufruf von increment_counter()
    # wie gewohnt funktionieren.
    # TODO: Erstellen Sie hier das Closure.
    increment_counter()
    increment_counter()
    increment_counter()
