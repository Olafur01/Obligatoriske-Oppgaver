# Oppgave 2.1
# Begynner med å importere CSV modulen, ettersom denne kommer til å gjøre det enklere for meg og åpne 
# slike filer
import csv

# Definerer den første funksjonen som er for åpning av filer. Her brukes with funksjonen for å åpne filer
# ettersom da trenger man ikke ha en close statement. Alt som er indented etter denne funksjon vil da være
# gjennomføres mens vilen er åpen. Bruker deretter csv.reader for å kunne se gjennom filen og gjør den om
# til en liste. Definerer så ordboken, før de måneden blir satt som key, og temperaturen blir satt som 
# verdiene. 
def open_csv(fil):
    with open(fil) as temperature_file:
        reader = csv.reader(temperature_file)
        temperature = {}
        for value in reader:
            temperature[value[0]] = float(value[1]) # bruker float for å klassifisere temp som et tall ikke en string
    return temperature


print(open_csv("max_temperatures_per_month.csv"))

# Oppgave 2.2
# Har oppgave 2 skrevet her, men har puttet det som en multiline comment. Tar først og åpner filen på lignende
# måte som i den tidligere deloppgaven. Kaller funksjonen med parameteren ordbok, som kjører funksjonen fra 
# forrige oppgave på max temp for månedene, og åpner temperaturfilen for 2018 innad i denne funksjonen. Tar så
# og looper gjennom både ordboken og listen, og ser først om det er lignende måneder. Hvis måneden er like, ser
# jeg så på om temperaturen for månedene i temperature_filen er større en det som har blitt skrevet før. Hvis 
# dette skjer så printes setningen om at dette har skjedd, og skriver temperaturen dette var målt med og når. 
'''
def nye_varme_rekord(ordbok, fil):
    with open(fil) as temperature_file:
        reader = csv.reader(temperature_file)
        for temperatures in reader:
            for old_temp in ordbok.items():
                if temperatures[0] == old_temp[0]:
                    if float(temperatures[2]) > float(old_temp[1]):
                        print(
                            f"Ny varme rekord på {temperatures[1]} {temperatures[0]}: {temperatures[2]} grader Celcius (gammel varmerekort for {old_temp[0]} var {old_temp[1]} grader Celcius) ")
                    else:
                        pass
                else:
                    pass


nye_varme_rekord(open_csv("max_temperatures_per_month.csv"),
                 "max_daily_temperature_2018.csv")
'''

# Oppgave 2.3
# Her kjøres oppgaven på nytt, bare denne gangen så oppdates ordboken isteden for å printe ut noe til terminalen 
def nye_varme_rekord(ordbok, fil):
    with open(fil) as temperature_file:
        reader = csv.reader(temperature_file)
        for temperatures in reader:
            for old_temp in ordbok.items():
                if temperatures[0] == old_temp[0]:
                    # Hvis det viser seg at en temperatur for en måned er større, oppdateres ordboken med denne
                    # temperaturen
                    if float(temperatures[2]) > float(old_temp[1]):
                        ordbok[old_temp[0]] = temperatures[2] 
                    else:
                        pass
                else:
                    pass
        return ordbok


print(nye_varme_rekord(open_csv("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv"))
# Kaller funksjonen laget i oppgave 2.3 og setter den lik variabelen ordbok. Grunnen for dette er fordi jeg 
# vil bruke den i oppg 2.4, som parameteren for ordbok. 
ordbok = nye_varme_rekord(open_csv("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv")

# Oppgave 2.4
# Lager funksjonen med to parameter, men denne gangen når jeg åpner filen så legger jeg til "w" i open funksjonen
# fordi da vil jeg åpne filen i write modus. Dette må gjøres hvis jeg vil skrive en ny fil. Tar deretter å lager
# en liste, der måneden blir satt før kommaen og temperaturen etter. 
def lag_csv_fil_av_ordbok(ordbok, ny_fil):
    with open('ny_temperatur_fil.csv', 'w') as ny_fil:
        writer = csv.writer(ny_fil)
        for key, value in ordbok.items():
            writer.writerow([key, value])
    

lag_csv_fil_av_ordbok(ordbok, 'ny_csv_fil.csv')
