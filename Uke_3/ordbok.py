'''
HUSK at man skal lese in gjennom bruker input 
'''
butikk_varer_og_priser = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(butikk_varer_og_priser)

def nye_vare_og_pris():
    vare = input("Hvilken vare vil du legge til? ")
    pris = input("Hvilken pris har denne varen? ")
    butikk_varer_og_priser[vare] = pris
    
nye_vare_og_pris()
nye_vare_og_pris()
print(butikk_varer_og_priser)
