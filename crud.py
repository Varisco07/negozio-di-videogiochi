import os
import json
 
catalogo_giochi = []
 
def leggi_file():
        global catalogo_giochi
        with open("./giochi.json", "r") as file:
            catalogo_giochi = json.load(file)
 
 
def scrivi_file():
        with open("./giochi.json", "w") as file:
            json.dump(catalogo_giochi, file)
 
 
def stampa_catalogo(catalogo):
    try:
        print("-" * 49)
        print(f"| {'ID':<2} | {'TITOLO':<40} |")
        print("-" * 49)
        count = 0
        while count < len(catalogo):
            print(f"| {count:<2} | {catalogo[count]['titolo']:<40} |")
            print("-" * 49)
            count += 1
    except Exception as err:
        print("\033[31mErrore durante la stampa del catalogo: \033[0m", err)
 
 
def stampa_gioco(gioco):
    try:
        stampa_catalogo(catalogo_giochi)
        numero = int(input("Inserisci il numero del gioco che vuoi vedere: "))
        print()
        print()
        print("-" * 59)
        print(f'| TITOLO        | {catalogo_giochi[numero]["titolo"]:<40}|')
        print("-" * 59)
        print(f'| SVILUPPATORE  | {catalogo_giochi[numero]["sviluppatore"]:<40}|')
        print("-" * 59)
        print(f'| ANNO          | {catalogo_giochi[numero]["anno"]:<40}|')
        print("-" * 59)
        print(f'| GENERE        | {catalogo_giochi[numero]["genere"]:<40}|')
        print("-" * 59)
        print(f'| COSTO         | {catalogo_giochi[numero]["costo"]:<40}|')
        print("-" * 59)
        print("\033[32mOperazione di visualizzazione gioco completata.\033[0m")
    except Exception as err:
        print("\033[31mErrore: \033[0m", err)
 
 
 
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
        costo = float(input("Inserisci il costo: "))
        catalogo.append({
            "titolo": titolo,
            "sviluppatore": sviluppatore,
            "anno": anno,
            "genere": genere,
            "costo": costo
        })
        print("\033[32mGioco aggiunto con successo\033[0m")
    except Exception as err:
        print("\033[31mErrore: \033[0m", err)
 
def rimuovi_gioco(catalogo):
    try:
        stampa_catalogo(catalogo)
        numero = int(input("Inserisci il numero del gioco da eliminare: "))
        catalogo.pop(numero)
        print("\033[32mGioco rimosso con successo\033[0m")
    except Exception as err:
        print("\033[31mErrore: \033[0m", err)
 
 
def modifica_gioco(catalogo):
    try:
        stampa_catalogo(catalogo)
        scelta = int(input("Inserisci il numero del gioco da modificare: "))
        gioco = catalogo[scelta]
       
        while True:
            print("Quale campo vuoi modificare?  ")
            print("+----------------------------+")
            print("| 1  | TITOLO                |")
            print("+----------------------------+")
            print("| 2  | SVILUPPATORE          |")
            print("+----------------------------+")
            print("| 3  | ANNO DI USCITA        |")
            print("+----------------------------+")
            print("| 4  | GENERE                |")
            print("+----------------------------+")
            print("| 5  | COSTO                 |")
            print("+----------------------------+")
            print("| 6  | TERMINA MODIFICHE     |")
            print("+----------------------------+")
            scelta = int(input("Inserisci il numero del campo da modificare: "))
           
            if scelta == 1:
                titolo = input("Inserisci il nuovo titolo: ")
                gioco["titolo"] = titolo
            elif scelta == 2:
                sviluppatore = input("Inserisci il nuovo sviluppatore: ")
                gioco["sviluppatore"] = sviluppatore
            elif scelta == 3:
                anno = int(input("Inserisci il nuovo anno di uscita: "))
                gioco["anno"] = anno
            elif scelta == 4:
                genere = input("Inserisci il nuovo genere: ")
                gioco["genere"] = genere
            elif scelta == 5:
                costo = float(input("Inserisci il nuovo costo: "))
                gioco["costo"] = costo
            elif scelta == 6:
                break
            else:
                print("\033[31mCampo non valido. Riprova.\033[0m")
 
        catalogo[scelta] = gioco
        print("\033[32mGioco modificato con successo\033[0m")
    except Exception as err:
        print("\033[31mErrore: \033[0m", err)
 
 
def giochi_per_sviluppatore(catalogo, sviluppatore):
    try:
        i = 0
        count = 0
        trovato = False
        while count < len(catalogo):
            if catalogo[count]["sviluppatore"].lower() == sviluppatore.lower():
                print(f"Ecco l'elenco dei giochi sviluppati da: {sviluppatore}")
                print("-" * 49)
                print(f"| {'ID':<2} | {'TITOLO':<40} |")
                print("-" * 49)
                trovato = True
                break
            count+=1
        while i < len(catalogo):
            if catalogo[i]["sviluppatore"].lower() == sviluppatore.lower():
                print(f"| {i:<2} | {catalogo[i]['titolo']:<40} |")
                print("-" * 49)
            i += 1
        if trovato == False:
            print("\033[31mNessun gioco trovato dallo sviluppatore inserito\033[0m")
    except Exception as err:
        print("\033[31mErrore durante la ricerca dei giochi per sviluppatore: \033[0m", err)
 
def giochi_in_periodo(catalogo, anno_inizio, anno_fine):
    try:
        i = 0
        count = 0
        trovato = False
        while count < len(catalogo):
            if anno_inizio <= catalogo[i]["anno"] <= anno_fine:
                print("Ecco l'elenco dei giochi usciti nel periodo scelto:")
                print("-" * 57)
                print(f"| {'TITOLO':<40} | {'ANNO':<10} |")
                print("-" * 57)
                trovato = True
                break
            count+=1
        while i < len(catalogo):
            if anno_inizio <= catalogo[i]["anno"] <= anno_fine:
                print(f"| {catalogo[i]['titolo']:<40} | {catalogo[i]['anno']:<10} |")
                print("-" * 57)
            i += 1
        if trovato == False:
            print("\033[31mNessun gioco trovato nel periodo inserito\033[0m")
    except Exception as err:
        print("\033[31mErrore durante la ricerca dei giochi per periodo: \033[0m", err)
 
 
def listino_prezzi_crescente(catalogo):
    try:
        n = len(catalogo)
        i = 0
        while i < n - 1:
            count = 0
            while count < n - 1 - i:
                if catalogo[count]["costo"] > catalogo[count + 1]["costo"]:
                    catalogo[count], catalogo[count + 1] = catalogo[count + 1], catalogo[count]
                count += 1
            i += 1
 
        print("Ecco l'elenco dei costi in ordine crescente nel periodo scelto:")
        print("-" * 57)
        print(f"| {'TITOLO':<40} | {'COSTO':<10} |")
        print("-" * 57)
       
        for gioco in catalogo:
            print(f"| {gioco['titolo']:<40} | {gioco['costo']:<10} |")
            print("-" * 57)
    except Exception as err:
        print("\033[31mErrore: \033[0m", err)
 
 
def costo_gioco(catalogo, costo_min, costo_max):
        try:
            i = 0
            count = 0
            trovato = False
            while count < len(catalogo):
                if costo_min <= catalogo[i]["costo"] <= costo_max:
                    print("Ecco l'elenco dei giochi usciti nel periodo scelto:")
                    print("-" * 57)
                    print(f"| {'TITOLO':<40} | {'COSTO':<10} |")
                    print("-" * 57)
                    trovato = True
                    break
                count+=1
            while i < len(catalogo):
                if costo_min <= catalogo[i]["costo"] <= costo_max:
                    print(f"| {catalogo[i]['titolo']:<40} | {catalogo[i]['costo']:<10} |")
                    print("-" * 57)
                i += 1
            if trovato == False:
                print("\033[31mNessun gioco trovato con il range di costo inserito\033[0m")
        except Exception as err:
            print("\033[31mErrore durante la ricerca dei giochi per periodo: \033[0m", err)
 
def giochi_per_genere(catalogo, genere):
    try:
        i = 0
        count = 0
        trovato = False
        while count < len(catalogo):
            if catalogo[count]["genere"].lower() == genere.lower():
                print(f"Ecco l'elenco dei giochi del seguente genere: {genere}")
                print("-" * 49)
                print(f"| {'ID':<2} | {'TITOLO':<40} |")
                print("-" * 49)
                trovato = True
                break
            count+=1
        while i < len(catalogo):
            if catalogo[i]["genere"].lower() == genere.lower():
                print(f"| {i:<2} | {catalogo[i]['titolo']:<40} |")
                print("-" * 49)
            i += 1
        if trovato == False:
            print("\033[31mNessun gioco del seguente genere trovato\033[0m")
    except Exception as err:
        print("\033[31mErrore durante la ricerca dei giochi per genere: \033[0m", err)
 
def menu():
    leggi_file()
    while True:
        try:
            print("\033[34m   _____              __  __   ______    _____   _______    ____     _____  \033[0m")
            print("\033[34m  / ____|     /\\     |  \\/  | |  ____|  / ____| |__   __| |  __  |  |  __ | \033[0m")
            print("\033[34m | |  __     /  \\    | \\  / | | |__    | (____     | |    | |  | |  | |__| |\033[0m")
            print("\033[34m | | |_ |   / /\\ \\   | |\\/| | |  __|    \\___  |    | |    | |  | |  |  ___| \033[0m")
            print("\033[34m | |__| |  / ____ \\  | |  | | | |____   ____) |    | |    | |__| |  | |     \033[0m")
            print("\033[34m  \\_____| /_/    \\_\\ |_|  |_| |______| |______|    |_|    | ____ |  |_|   \033[0m")
           
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 0  | per terminare         \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 1  | per vedere un gioco   \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 2  | per vedere il catalogo\033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 3  | per aggiungere un gioco\033[34m |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 4  | rimuovere un gioco    \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 5  | modificare un gioco   \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 6  | giochi per sviluppatore\033[34m |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 7  | giochi per periodo    \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 8  | giochi per costo      \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 9  | giochi per genere     \033[34m  |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 10 | listino prezzi       \033[34m   |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
            print("\033[34m| \033[36m 11 | aggiorna file        \033[34m   |\033[0m")
            print("\033[34m+-------------------------------+\033[0m")
           
            scelta = int(input("\033[36m--> \033[0m"))
 
            if scelta == 0:
                break
            elif scelta == 1:
                stampa_gioco(catalogo_giochi)
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
            elif scelta == 8:
                costo_min = float(input("Inserisci il costo minimo del gioco: "))
                costo_max = float(input("Inserisci il costo massimo del gioco: "))
                costo_gioco(catalogo_giochi, costo_min, costo_max)
            elif scelta == 9:
                genere = input("Inserisci il genere di giochi che vuoi visualizzare: ")
                giochi_per_genere(catalogo_giochi, genere)
            elif scelta == 10:
                listino_prezzi_crescente(catalogo_giochi)
            elif scelta == 11:
                scrivi_file()
                print("\033[32mFile scritto con successo\033[0m")
            else:
                print("\033[31mScelta non valida\033[0m")
        except Exception as err:
            print("\033[31mErrore: \033[0m", err)
        finally:
            input("premere un tasto per continuare...")
            os.system("cls")
           
menu()
 
