''' Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil 
(som du lager selv og leverer sammen med de andre filene) der hver linje beskriver et navn 
på et mål og selve målet i tommer. Formatet vil se slik ut:  

Skulderbredde 4 
Halsvidde 3.2 
Livvidde 10  
Hint : du kan bruke funksjonen . split() for å gjøre dette.  

La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboken. 
Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av 
tommerTilCm som du skrev tidligere for å skrive ut målene i centimeter'''
import csv

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

def open_csv(fil):
    with open(fil) as temperature_file:
        reader = csv.reader(temperature_file, delimiter = " ")
        maal = {}
        for items in reader:
            maal[items[0]] = float(items[1])
    return maal

maal = (open_csv("Example_text.csv"))

print(maal)

for tommer in maal.values():
    print(f"{tommer} i tommer er {round(tommerTilCm(tommer),2)} i centimeter")
