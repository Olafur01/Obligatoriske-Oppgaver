# Oppgave 4.1 
# For å telle mengde med bokstaver så bruker jeg bare len() funksjonen, som er en innebygd funksjon. 
def bokstavtelling(ord):
    return len(ord)

# Oppgave 4.2 
# Lagde først en liste, ved bruken av split funksjonen, som splitter basert på mellomrom. Er derfor jeg legger
# til ekstra mellomrom for å tegnsettingene. Jeg vil først bare a key verdiene for ordboken. Derfor gjøre jeg 
# listen om til en ordbok, for så om til en liste igjen, slik at det blir enklere å jobbe med, og har bare unike
# verdier. 
def ordbok(setning):
    setning = setning.replace(",", " , ") # Jeg legger til et mellomrom før og etter komma 
    setning = setning.replace(".", " . ") # Jeg legger til et mellomrom før og etter punktum
    setning = setning.replace("!", " ! ") # Jeg legger til et mellomrom før og etter utropstegn
    setning = setning.replace("?", " ? ") # Jeg legger til et mellomrom før og etter spørsmålstegn 
    liste = setning.lower().split() # Gjør alle elementene om til lower, så det er letter å sammenligne de 
    keys_for_ordbok = list(dict.fromkeys(liste)) # For aa fjerne duplicates. Vurderte aa gjore om til mengde, men da mister man rekkefolgen
    ordbok = {}
    for key in keys_for_ordbok:
        count = liste.count(key) # Finner først mengde ganger et ord oppstår i listen, ved bruk av count funksjonen 
        ordbok[key] = count # Legger til hver key og dens korresponderende count inn i ordboken. 
    return ordbok 

# Oppgave 4.3
# Jeg legger igjen til ekstra mellomrom for tegnsetting, slik at når dette blir splittet opp i en liste 
# så blir dette sitt eget element. Da blir det rikitig lengde på den som skrives inn av bruker. 
setning = input("Skriv en setning: ")
setning = setning.replace(",", " , ") # Jeg legger til et mellomrom før og etter komma 
setning = setning.replace(".", " . ") # Jeg legger til et mellomrom før og etter punktum
setning = setning.replace("!", " ! ") # Jeg legger til et mellomrom før og etter utropstegn
setning = setning.replace("?", " ? ") # Jeg legger til et mellomrom før og etter spørsmålstegn 

print("Det er {} ord i setningen din".format(len(setning.split())))

# Jeg lager en ny variabel kalt ordbok, som ordbok funksjonen jeg lagde tidligere blir tildelt til slik at 
# verdien der blir returnert til denne variablene. Det samme gjøres med counter_bokstaver og bokstavtelling
# funksjonen. Bruker deretter en for loop for å gå gjennom alle key ordene i ordboken, for så å telle hvor
# mange ganger dette ordet brukes og hvor mange bokstaver den består av. 
ordbok = ordbok(setning) 
for ord in ordbok.keys():
    counter_bokstaver = bokstavtelling(ord)
    print("Ordet '{}' forekommer {} ganger, og har {} bokstaver".format(ord, ordbok[ord], counter_bokstaver))