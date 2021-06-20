# Definerer klassen celle
class Celle:
   # Oppretter konstruktoeren, hvor statusen for cellen blir satt til dø med en gang.
    def __init__(self):
        self._status = "død"

    # Instansmetode der man kan sette status til dø
    def settDoed(self):
        self._status = "død" 

    # Instansmetode der man setter status til levende 
    def settLevende(self):
        self._status = "levende" 

    # Instansmetode der man kan sjekke om cellen er i livet eller ikke 
    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False 

    # Instansmetode for aa hente statustegn, der levende returnerer "O", mens død returnerer "."     
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else:    
            return "."

