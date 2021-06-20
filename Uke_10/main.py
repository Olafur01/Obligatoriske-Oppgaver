from spillebrett import Spillebrett

# Oppretter en funksjon som simulerer en generasjon, og som kan kalles av 
# hovedfunksjonen hvis brukeren vil gjennomføre en ny runde 
def simulere(brett):
    brett.oppdatering()
    brett.tegnBrett()
    brett.skrivInfo()

# Oppretter hovedfunksjonen som bruker klassen spillebrett for å 
# lage og gjennomfoere "Game of Life"
def main():
    rader = input("Skriv inn antall rader, som er et positivt heltall:\n> ")
    kolonner = input("Skriv inn antall kolonner, som er et positivt heltall:\n> ")
    # Sjekker om det er riktig input fra brukeren ved å se at de skriver inn et tall
    # og at den ikke er lik 0. Isdigit funksjonen returnerer true hvis en input er et tall 
    # som er 0 eller større. 
    if rader.isdigit() == False or kolonner.isdigit() == False or rader == "0" or kolonner == "0":
        print("Input er feil! Skriv inn paa nytt.")
        main()
    # Hvis det er riktig input så vil programmet kjøres
    else:
        brett = Spillebrett(int(rader), int(kolonner))
        brett.tegnBrett()
        brett.skrivInfo()
        cont = True
        # Oppretter en while loekke hvor spille fortsetter til bruker avslutter ved å taste 
        # 'q'
        while cont:
            bruker_valg = input("Press 'q' for å avslutte. Tast noe annet for aa fortsette:\n> ")
            if bruker_valg != 'q':
                simulere(brett)
            else:
                print("Goodbye")
                cont = False
4
# Kaller på hovedprogrammet 
main()