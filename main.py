"""Refactoring: Vermeiden globaler Variablen durch Closures.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu05/aufgaben/closures2
"""

def create_counter():
    """
    Erstellt einen Counter, der bei jedem Aufruf um 1 erhöht wird.

    :return: Wert des Counters
    """
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1
        print(f"Counter: {counter}")
        return counter

    return increment_counter


if __name__ == "__main__":
    # Auch mit dem Closure soll der Aufruf von demo_increment_counter() wie gewohnt funktionieren.
    demo_increment_counter = create_counter()

    demo_increment_counter()
    demo_increment_counter()
    demo_increment_counter()
