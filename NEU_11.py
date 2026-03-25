


while True:
   # eingabe = input("Zahl: ")
    eingabe = 44

    try:
        ergebnis = 100 / float(eingabe)


    except ZeroDivisionError:
        print("Durch 0 geteilt")
    except ValueError:
        print("Du hast keine gültige Zahl eingegeben")
    except:
        print("Irgendein Fehler")

    else:
        print(ergebnis)
        break



while True:
    eingabe = "ff"
    try:
        ergebnis = 1/int(eingabe)
    except:
        print("Fehler, Feierabend!")
        break  # oder continue
    else:
        print(ergebnis)
        break
    finally:
        print("Ich räume hier auf")
    print("Programm geht weiter")