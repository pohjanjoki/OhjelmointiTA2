# Funktio painoindeksin (body mass index) laskemiseksi
def bmi(paino, pituus):
    painoindeksi = paino / pituus ** 2
    return painoindeksi

# Funktio kehon rasvaprosentin laskemiseksi

def rasvaprosentti(bmi, ika, sukupuoli):
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti


# Kysytään käyttäjältä tarvittavat tiedot, huom näppäistöstä saadaan aina merkkijono (string)
paino_str = input('Anna painosi kilogrammoina: ')
pituus_str = input('Anna pituutesi metreinä: ')
ika_str = input('Kuinka vanha olet: ')
sukupuoli_str = input('Paina 1, jos olet mies, 0 jos olet nainen: ')

# Muutetaan merkkijonot luvuiksi
# Muuttuja, johon tallentuu tieto virheen tapahtumisesta alustus: False
tapahtui_virhe = False

# Virheenkäsittelyrutiini
try:
    # Tutkitaan onko merkkijonossa aakkosia ja annetaan tyyppivirhe jos on
    if paino_str.isalpha():
        raise TypeError('Vain numerot (0..9) ja desimaalipiste(.) on sallittu')

    # Jos ei ole virhettä, muutetaan liukuluvuksi
    paino = float(paino_str)

# Jos tapahtui virhe, tulostetaan virheilmoitusteksti ja asetteaan virhemuuttujan arvoksi True    
except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

# TODO: tee tyyppitarkistusrutiinit kaikille muuttujille
try:
    pituus = float(pituus_str)
except:
    print('Pituus virheellinen')
    tapahtui_virhe = True

try:
    ika = float(ika_str)
except:
    print('Ikätieto virheellinen')
    tapahtui_virhe = True

try:
    sukupuoli = float(sukupuoli_str)
except:
    print('sukupuoli virheellinen, syötä vain 1 tai 0')
    tapahtui_virhe = True

if tapahtui_virhe == False:
    painoindeksi = bmi(paino, pituus)
    print('Painoindeksisi on:', painoindeksi)
    rprosentti = rasvaprosentti(painoindeksi, ika, sukupuoli)
    print('Kehosi rasvaprosentti on:', rprosentti)
else:
    print('Tuloksia ei voitu laskea, koska syöttötiedoissa oli virhe')