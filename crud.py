import os
 
 
catalogo_giochi = [
    {
        "titolo": "The Legend of Zelda: Breath of the Wild",
        "sviluppatore": "Nintendo",
        "anno": 2017,
        "genere": "Action-Adventure"
    },
    {
        "titolo": "God of War",
        "sviluppatore": "Santa Monica Studio",
        "anno": 2018,
        "genere": "Action"
    },
    {
        "titolo": "FC 25",
        "sviluppatore": "Electronic Arts",
        "anno": 2024,
        "genere": "Sport"
    }
]
 
 
def stampa_catalogo(catalogo):
    try:
        print(f"{'ID'} | {'TITOLO':<39} |")
        print("-" * 46)
        count = 0
        while count < len(catalogo):
            print(f"{count} | {catalogo[count]['titolo']:<40} |")
            print("-" * 46)
            count += 1
    except Exception as err:
        print("Errore durante la stampa del catalogo: ", err)
 
 
 
def aggiungi_gioco(catalogo):
    try:
        count = 0
        titolo = input("Inserisci il titolo: ")
        while count < len(catalogo):
            if catalogo[count]["titolo"] == titolo:
                print("Errore: Gioco già presente.")
                return
            count += 1
        sviluppatore = input("Inserisci il nome dello sviluppatore: ")
        anno = int(input("Inserisci l'anno di uscita: "))
        genere = input("Inserisci il genere: ")
        catalogo.append({
            "titolo": titolo,
            "sviluppatore": sviluppatore,
            "anno": anno,
            "genere": genere
        })
        print("Gioco aggiunto con successo")
    except Exception as err:
        print("Errore: ", err)


 
 
def rimuovi_gioco(catalogo):
    try:
        stampa_catalogo(catalogo)
        numero = int(input("Inserisci il numero del gioco da eliminare: "))
        catalogo.pop(numero)
        print("Gioco rimosso con successo")
    except Exception as err:
        print("Errore: ", err)
 
 
def modifica_gioco(catalogo):
    try:
        stampa_catalogo(catalogo)
        numero = int(input("Inserisci il numero del gioco da modificare: "))
        titolo = input("Inserisci il nuovo titolo: ")
        sviluppatore = input("Inserisci il nuovo sviluppatore: ")
        anno = int(input("Inserisci il nuovo anno di uscita: "))
        genere = input("Inserisci il nuovo genere: ")
 
        catalogo[numero] = {
            "titolo": titolo,
            "sviluppatore": sviluppatore,
            "anno": anno,
            "genere": genere
        }
        print("Gioco modificato con successo")
    except Exception as err:
        print("Errore: ", err)

 
 
def giochi_per_sviluppatore(catalogo, sviluppatore):
    try:
        print(f"Ecco l'elenco dei giochi sviluppati da: {sviluppatore}")
        i = 0
        while i < len(catalogo):
            if catalogo[i]["sviluppatore"].lower() == sviluppatore.lower():
                print(catalogo[i])
            i += 1
    except Exception as err:
        print("Errore durante la ricerca dei giochi per sviluppatore: ", err)
 
 
def giochi_in_periodo(catalogo, anno_inizio, anno_fine):
    try:
        print("Ecco l'elenco dei giochi usciti nel periodo scelto:")
        i = 0
        while i < len(catalogo):
            if anno_inizio <= catalogo[i]["anno"] <= anno_fine:
                print(catalogo[i])
            i += 1
    except Exception as err:
        print("Errore durante la ricerca dei giochi per periodo: ", err)
 
 
def menu():
    while True:
        try:
            print("   _____              __  __   ______    _____   _______    ____     _____  ")
            print("  / ____|     /\\     |  \\/  | |  ____|  / ____| |__   __| |  __  |  |  __ | ")
            print(" | |  __     /  \\    | \\  / | | |__    | (____     | |    | |  | |  | |__| |")
            print(" | | |_ |   / /\\ \\   | |\\/| | |  __|    \\___  |    | |    | |  | |  |  ___| ")
            print(" | |__| |  / ____ \\  | |  | | | |____   ____) |    | |    | |__| |  | |     ")
            print("  \\_____| /_/    \\_\\ |_|  |_| |______| |______|    |_|    | ____ |  |_|   ")
 
            scelta = int(input("0. per terminare\n"
                               "1. per vedere un gioco\n"
                               "2. per vedere il catalogo\n"
                               "3. per aggiungere un gioco\n"
                               "4. rimuovere un gioco\n"
                               "5. modificare un gioco\n"
                               "6. giochi per sviluppatore\n"
                               "7. giochi per periodo\n--> "))
            if scelta == 0:
                break
            elif scelta == 1:
                try:
                    stampa_catalogo(catalogo_giochi)
                    numero = int(input("Inserisci il numero del gioco che vuoi vedere: "))
                    print(f'TITOLO       | {catalogo_giochi[numero]["titolo"]:<30}|')
                    print("-" * 46)
                    print(f'SVILUPPATORE | {catalogo_giochi[numero]["sviluppatore"]:<30}|')
                    print("-" * 46)
                    print(f'ANNO         | {catalogo_giochi[numero]["anno"]:<30}|')
                    print("-" * 46)
                    print(f'GENERE       | {catalogo_giochi[numero]["genere"]:<30}|')
                    print("-" * 46)
                except Exception as err:
                    print("Errore: ", err)
                finally:
                    print("Operazione di visualizzazione gioco completata.")
            elif scelta == 2:
                stampa_catalogo(catalogo_giochi)
            elif scelta == 3:
                aggiungi_gioco(catalogo_giochi)
            elif scelta == 4:
                rimuovi_gioco(catalogo_giochi)
            elif scelta == 5:
                modifica_gioco(catalogo_giochi)
            elif scelta == 6:
                sviluppatore = input("Inserisci il nome dello sviluppatore: ")
                giochi_per_sviluppatore(catalogo_giochi, sviluppatore)
            elif scelta == 7:
                anno_inizio = int(input("Inserisci l'anno di inizio: "))
                anno_fine = int(input("Inserisci l'anno di fine: "))
                giochi_in_periodo(catalogo_giochi, anno_inizio, anno_fine)
            else:
                print("Scelta non valida")
        except Exception as err:
            print("Errore: ", err)
        finally:
            input("Premi un tasto per continuare...")
            os.system("cls")
            
menu()