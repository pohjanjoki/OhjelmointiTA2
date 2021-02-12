# Kirjasto, jossa on tietojen järkevyystarkistukseen soveltuvia funktioita

# 1. Poistetaan tekstistä ylimääräiset merkit, kuten välilyönnit alusta ja lopusta
# 2. Vaihdetaan vahingossa syötetty desimaalipilkku (,) desimaalipisteeksi (.)
# 3. Määritellään järkevän arvon alaraja (pienin hyväksyttävä arvo)
# 4. Määritellään järkevän arvon yläraja (suurin hyväksyttävä arvo)

def on_jarkeva(syote, alaraja, ylaraja):
    
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit ja selvittää, onko syötetty arvo annettujen rajojen sisällä. Funktio muuttaa desimaalipilkun desimaalipisteeksi.

    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alaraja (float): Pienin sallittu arvo
        ylaraja (float): Suurin sallittu arvo
    """
    
    # Poistetaan tyhjät merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    # Poistetaan tyhjät merkit merkkijonon lopusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # Selvitetään, onko merkkijonossa pilkku
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy, se korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
        korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot ovat sallittu')
        luku = 0

    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print('Virheilmoitus')

    # Tarkistetaan, eteti syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print('Virheilmoitus')

    # Palautetaan luku
    return luku


# Testetaan toiminta
tulos = on_jarkeva('sata', 1, 500)
print(tulos)