deutsche_woerter = ["Hund", "Katze", "Baum", "Haus"]
englische_woerter = ["dog", "cat", "tree", "house"]

deutsches_wort = input("Gib ein deutsches Wort ein: ")

try:
    index = deutsche_woerter.index(deutsches_wort)
    englisches_wort = englische_woerter[index]
    print("Das englische Wort ist:", englisches_wort)
except ValueError:
    print("Das eingegebene deutsche Wort ist nicht in der Liste vorhanden.")