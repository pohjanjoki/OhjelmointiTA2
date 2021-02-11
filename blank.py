# Funktio kehon painoindeksin (BMI) laskemiseen
def bmi(paino, pituus):
    painoindeksi = paino / pituus ** 2
    return painoindeksi

# Funktio kehon rasvaprosentin laskemiseen
def rasvaprosentti(bmi, ika, sukupuoli):
    aikuisen_rasvaprosentti = (1.20 * bmi) + (0.23 * ika) - (10.8 * sukupuoli) - 5.4
    return aikuisen_rasvaprosentti

# Kysytään käyttäjältä tarvittavat tiedot (Huom! Näppäimistöstä saadaan aina merkkijono (string))
paino_str = input('Anna paino kilogrammoina: ')
pituus_str = input('Anna pituus metreinä: ')
ika_str = input('Anna ikä vuosina: ')
sukupuoli_str = input('Anna sukupuoli (1 = mies, 0 = nainen: ')

# Muutetaan merkkijonot luvuiksi
paino = float(paino_str)
pituus = float(pituus_str)
ika = float(ika_str)
sukupuoli = float(sukupuoli_str)

# Lasketaan painoindeksi kysyttyjen tietojen perusteella
bmi = bmi(paino,pituus)

# Lasketaan rasvaprosentti
rasvaprosentti = rasvaprosentti(bmi, ika, sukupuoli)
print('Rasvaprosentti on', rasvaprosentti)

try:
    print(x)
except Exception as e:
    
finally:
    pass