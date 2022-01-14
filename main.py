#zgadywanie liczby
szukanaLiczba = 134
zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Odgadnij szukaną liczbę "))

    if (szukanaLiczba == zgadywanaLiczba):
        print ("BRAWO ODGADŁEŚ NASZĄ LICZBĘ!!! WYGRAŁEŚ ŻELAZKO!!!")
    elif (szukanaLiczba < zgadywanaLiczba):
          print ("Liczba jest ZA DUŻA, spóbuj MNIEJSZEJ")
    elif (szukanaLiczba > zgadywanaLiczba):
        print ("Podana liczba jest ZA MAŁA, spróbuj WIĘKSZEJ")
    else:
        print ("Spróbuj raz jeszcze")