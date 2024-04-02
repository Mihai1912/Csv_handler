import csv
import pandas as pd
from IPython.display import display

# def detecteaza_delimitator(nume_fisier):
#     with open(nume_fisier, 'r', encoding='utf-8') as fisier:
#         prima_linie = fisier.readline()
#         if ',' in prima_linie:
#             return ','
#         elif ';' in prima_linie:
#             return ';'
#     return ','  # Implicit, considerăm virgula ca delimitator dacă nu găsim altul


# def citeste_csv(nume_fisier):
#     # Creăm o listă goală pentru a stoca rândurile
#     continut = []
#     delinitator = detecteaza_delimitator(nume_fisier)
#     # Deschidem fișierul CSV în modul de citire
#     with open(nume_fisier, mode='r', encoding='utf-8') as fisier:
#         # Creăm un cititor CSV care să trateze corect ghilimelele
#         cititor_csv = csv.reader(fisier, delimiter=delinitator, quotechar='"')
#         # Iterăm prin fiecare rând din fișierul CSV
#         for rand in cititor_csv:
#             # Adăugăm rândul citit la lista de conținut
#             continut.append(rand)
#     # Returnăm conținutul citit
#     return continut

def detecteaza_delimitator(nume_fisier):
    with open(nume_fisier, 'r', encoding='utf-8') as fisier:
        prima_linie = fisier.readline()
        if ',' in prima_linie:
            return ','
        elif ';' in prima_linie:
            return ';'
    return ','  # Implicit, considerăm virgula ca delimitator dacă nu găsim altul

def proceseaza_rand(rand, delimitator):
    # Să înlăturăm ghilimelele escapate și să splităm manual, luând în considerare delimitatorul
    # Înlocuim \" cu un placeholder unic (spre exemplu, UUID sau un șir improbabil de întâlnit)
    placeholder = "\uF8FF"  # Exemplu de caracter rar utilizat
    rand_modificat = rand.replace('\"', placeholder)
    
    # Acum putem să splităm sigur pe baza delimitatorului
    elemente = rand_modificat.split(delimitator)
    
    # Înlocuim placeholder-ul înapoi cu ghilimele escapate
    elemente = [elem.replace(placeholder, '\"') for elem in elemente]
    return elemente

def citeste_csv_personalizat(nume_fisier):
    continut = []
    delimitator = detecteaza_delimitator(nume_fisier)
    
    with open(nume_fisier, 'r', encoding='utf-8') as fisier:
        for linie in fisier:
            rand_procesat = proceseaza_rand(linie.strip(), delimitator)
            continut.append(rand_procesat)
    
    return continut

def elimitare_ufeff(text):
    return text.replace('\ufeff', '')

def custom_cross_join(table1, table2, table3):
    # Rezultatul join-ului: o listă de dicționare
    result = []
    
    # Iterăm prin fiecare combinație de rânduri dintre primele două tabele
    for row1 in table1:
        for row2 in table2:
            # Combinăm rândurile din primele două tabele
            combined_row12 = {**row1, **row2}
            for row3 in table3:
                # Apoi combinăm rezultatul cu fiecare rând din a treia tabelă
                combined_row123 = {**combined_row12, **row3}
                # Adăugăm rândul combinat în rezultat
                result.append(combined_row123)
                
    return result


def main ():
    facebook_dataset = 'facebook_dataset.csv'
    google_dataset = 'google_dataset.csv'
    website_dataset = 'website_dataset.csv'

    # facebook = citeste_csv(facebook_dataset)
    # google = citeste_csv(google_dataset)
    # website = citeste_csv(website_dataset)

    facebook = citeste_csv_personalizat(facebook_dataset)
    google = citeste_csv_personalizat(google_dataset)
    website = citeste_csv_personalizat(website_dataset)

    facebook[0][0] = elimitare_ufeff(facebook[0][0])
    google[0][0] = elimitare_ufeff(google[0][0])
    website[0][0] = elimitare_ufeff(website[0][0])

    facebook_header_index = {}
    for i in range(0, len(facebook[0])):
        facebook_header_index[facebook[0][i]] = i

    google_header_index = {}
    for i in range(0, len(google[0])):
        google_header_index[google[0][i]] = i

    website_header_index = {}
    for i in range(0, len(website[0])):
        website_header_index[website[0][i]] = i

    table1 = []
    table2 = []
    table3 = []

    # for i in range(1, len(facebook)):
    #     row = {}
    #     for key in facebook[0]:
    #         row[key] = facebook[i][facebook_header_index[key]]
    #     table1.append(row)

    print(google_header_index)

    for i in range(1, len(google)):
        row = {}
        for key in google[0]:
            print(google[i].__len__())
            if google[i].__len__() > 15:
                print(google[i])
                break
            row[key] = google[i][google_header_index[key]]
        table2.append(row)

    for i in range(1, len(website)):
        row = {}
        for key in website[0]:
            row[key] = website[i][website_header_index[key]]
        table3.append(row)

    print("\n====================================================================================================\n")

    merged_data = sorted(set(facebook[0] + google[0] + website[0]))

    display(merged_data)

    # display(facebook[:1])
    # print("\n")
    # display(google[:1])
    # print("\n")
    # display(website[:1])


if __name__ == '__main__':
    main()