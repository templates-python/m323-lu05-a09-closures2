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
    # Auch mit dem Closure soll der Aufruf von increment_counter() wie gewohnt funktionieren.
    increment_counter = create_counter()

    increment_counter()
    increment_counter()
    increment_counter()
