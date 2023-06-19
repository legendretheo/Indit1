try:
    zahl1 = int(input("Gib die erste Zahl ein: "))
    zahl2 = int(input("Gib die zweite Zahl ein: "))
    ergebnis = zahl1 / zahl2
    print("Das Ergebnis ist:", ergebnis)
except ValueError:
    print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")
except Exception as e:
    print("Ein unbekannter Fehler ist aufgetreten:", str(e))