#definicja funkcji pobierajacej 2 wyrazy z jednej linii pliku
def words(line):

    words = line.split()
    word1 = words[0]
    word2 = words[1]

    if word1.isascii() and word2.isascii():
        if word1.isalpha() and word2.isalpha():
            if word1.islower() and word2.islower():
                if len(word1)<=200 or len(word2)<=200:

                    global K, L
                    K = word1
                    L = word2
                    return K, L

    print("Wymagania dotyczace wyrazow nie zostaly spelnione.")
    exit(22)


# definicja funkcji anagramu
def Anagram(wordK, wordL):
    # usuwanie bialych znakow
    wordK = wordK.strip()
    wordL = wordL.strip()

    # tworzenie listy przechowujacej litery slow L i K
    lettersK = sorted(list(wordK))
    lettersL = sorted(list(wordL))

    # sprawdzanie czy slowo L jest anagramem slowa K
    if lettersL == lettersK:
        return "TAK"
    else:
        return "NIE"


#wyjasnienie dzialania programu dla uzytkownika, definicja anagramu wraz z przykladami
print("Program sprawdza czy zadane jako drugie slowo L jest anagramem zadanego najpierw slowa K.\n")
print("Anagramem slowa K nazywamy takie slowo L, ktore sklada sie z takich samych liter,\n"
      "co slowo K lecz w dowolnej kolejnosci.\n\n"
      "Przyklady:\n"
      "takt i tkat to anagramy,\n"
      "trawa i warta to anagramy,\n"
      "lista i atlas to nie anagramy.")
print("\nProgram zwraca TAK, jesli slowa to anagramy, a NIE, jesli nie sa anagramami.\n\n")
print("Nalezy podac 2 wyrazy w kazdej linii pliku input:"
          "\n- wyrazy musza skladac sie jedynie z malych liter alfabetu angielskiego"
          "\n- dlugosc slowa nie moze przekraczac 200 znakow"
          "\n- wyrazy musza byc oddzielone spacja"
          "\n - kazda para wyrazow musi znajdowac sie w osobnej lini\n\n")


#uruchomienie programu
try:
    with open("anagramyWynik.txt", "w") as file:
        with open("raport.txt", "a") as raport:
            with open("input.txt", "r") as inputFile:
                for line in inputFile:
                    words(line)
                    file.write(Anagram(K, L) + "\n")
                    raport.write(f"INPUT:\n{K}\n{L}\nOUTPUT:\n{Anagram(K,L)}\n-----------------------------------------------\n")
except:
    print("Wystapil blad w trakcie dzialania programu.")
    exit(56)