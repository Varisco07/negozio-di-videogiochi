from os import system

gioco1 = {
    "titolo": "The Legend of Zelda: Breath of the Wild",
    "sviluppatore": "Nintendo",
    "anno": 2017,
    "genere": "Action-Adventure"
}

gioco2 = {
    "titolo": "God of War",
    "sviluppatore": "Santa Monica Studio",
    "anno": 2018,
    "genere": "Action"
}

gioco3 = {
    "titolo": "FC 25",
    "sviluppatore": "Electronic arts",
    "anno": 2024,
    "genere": "Sport"
}

catalogoGiochi = [gioco1, gioco2, gioco3]

def stampaCatalogo(catalogo):
    for i, gioco in enumerate(catalogo):
        print(f"{i}.")
        print(f"TITOLO: {gioco['titolo']}")
        print(f"SVILUPPATORE: {gioco['sviluppatore']}")
        print(f"ANNO: {gioco['anno']}")
        print(f"GENERE: {gioco['genere']}")
        print()

def stampaGioco(gioco):
    print(f"TITOLO: {gioco['titolo']}")
    print(f"SVILUPPATORE: {gioco['sviluppatore']}")
    print(f"ANNO: {gioco['anno']}")
    print(f"GENERE: {gioco['genere']}")

def aggiungiGioco():
    try:
        titolo = input("Inserisci il titolo: ")
        sviluppatore = input("Inserisci il nome dello sviluppatore: ")
        anno = int(input("Inserisci l'anno di uscita: "))
        genere = input("Inserisci il genere: ")
        gioco = {
            "titolo": titolo,
            "sviluppatore": sviluppatore,
            "anno": anno,
            "genere": genere
        }
        catalogoGiochi.append(gioco)
        print("Gioco aggiunto con successo")
    except Exception as err:
        print("ERROR: ", err)
        return

def rimuoviGioco(catalogo):
    stampaCatalogo(catalogo)
    try:
        numero = int(input("Inserisci il numero del gioco da eliminare: "))
        catalogo.pop(numero)
        print("Gioco rimosso con successo")
    except Exception as err:
        print("ERROR: ", err)

def modificaGioco(catalogo):
    stampaCatalogo(catalogo)
    try:
        numero = int(input("Inserisci il numero del gioco da modificare: "))
        titolo = input("Inserisci il nuovo titolo: ")
        sviluppatore = input("Inserisci il nuovo sviluppatore: ")
        anno = int(input("Inserisci il nuovo anno di uscita: "))
        genere = input("Inserisci il nuovo genere: ")
        
        catalogo[numero]["titolo"] = titolo
        catalogo[numero]["sviluppatore"] = sviluppatore
        catalogo[numero]["anno"] = anno
        catalogo[numero]["genere"] = genere
        print("Gioco modificato con successo")
    except Exception as err:
        print("ERROR: ", err)
        return

def giochiPerSviluppatore(catalogo, sviluppatore):
    try: 
        print("Ecco l'elenco dei giochi sviluppati da:", sviluppatore)
        for gioco in catalogo:
            if gioco["sviluppatore"] == sviluppatore:
                print(f"{gioco}")
    except Exception as err:
        print("ERROR: ", err)
        return

def giochiInPeriodo(catalogo, annoInizio, annoFine):
    try: 
        print("Ecco l'elenco dei giochi usciti nel periodo scelto")
        for gioco in catalogo:
            if annoInizio <= gioco["anno"] <= annoFine:
                print(f"{gioco}")
    except Exception as err:
        print("ERROR: ", err)
        return

def menu():
    while True:
        try:
            print("   _____              __  __   ______    _____   _______    ____     _____  ")  
            print("  / ____|     /\\     |  \\/  | |  ____|  / ____| |__   __| |  __  |  |  __ | ")  
            print(" | |  __     /  \\    | \\  / | | |__    | (____     | |    | |  | |  | |__| |")  
            print(" | | |_ |   / /\\ \\   | |\\/| | |  __|    \\___  |    | |    | |  | |  |  ___| ")  
            print(" | |__| |  / ____ \\  | |  | | | |____   ____) |    | |    | |__| |  | |     ")  
            print("  \\_____| /_/    \\_\\ |_|  |_| |______| |______|    |_|    | ____ |  |_|   ")

            scelta = int(input("0. per terminare\n1. per vedere un gioco\n2. per vedere il catalogo\n3. per aggiungere un gioco\n4. rimuovere un gioco\n5. modificare un gioco\n6. giochi per sviluppatore\n7. giochi per periodo\n--> "))
            if scelta == 0:
                break
            elif scelta == 1:
                stampaCatalogo(catalogoGiochi)
                numero = int(input("Inserisci il numero del gioco che vuoi vedere: "))
                stampaGioco(catalogoGiochi[numero])
            elif scelta == 2:
                stampaCatalogo(catalogoGiochi)
            elif scelta == 3:
                aggiungiGioco()
            elif scelta == 4:
                rimuoviGioco(catalogoGiochi)
            elif scelta == 5:
                modificaGioco(catalogoGiochi)
            elif scelta == 6:
                sviluppatore = input("Inserisci il nome dello sviluppatore: ")
                giochiPerSviluppatore(catalogoGiochi, sviluppatore)
            elif scelta == 7:
                annoInizio = int(input("Inserisci l'anno di inizio: "))
                annoFine = int(input("Inserisci l'anno di fine: "))
                giochiInPeriodo(catalogoGiochi, annoInizio, annoFine)
            else:
                print("Scelta non valida")
            input("Premi un tasto per continuare...")
            system("cls")
        except Exception as err:
            print("ERROR: ", err)
            input("Premi un tasto per continuare...")
            system("cls")

menu()
