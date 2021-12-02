def hirsiPuu(oikea):
    tahtina = muutaTahdiksi(oikea)
    arvaukset = []
    elamat = 6

    while(True):
        tahtina, arvaukset, elamat = arvaa(oikea, tahtina, arvaukset, elamat)
        if tahtina == oikea:
            print('Voitit Pelin! Sana oli: ' + oikea)
            break
        elif elamat <= 0:
            print('Hävisit pelin! Oikea sana olisi ollut: ' + oikea)
            break
    
def muutaTahdiksi(sana):
    return '*'*len(sana)

def arvaa(oikea, tahtina, arvaukset, elamat):
    print('\n' + ('#'*10) + '\n')
    print('Elämiä jäljellä: ' + str(elamat))
    print('Arvatut kirjaimet: ', arvaukset)
    print(tahtina)
    arvaus = input('Arvaa kirjain tai sana: ')

    if len(arvaus) > 1:
        if arvaaSana(oikea, arvaus):
            tahtina = oikea
        else:
            elamat = 0
        return tahtina, arvaukset, elamat
    else:
        while(True):
            if arvaus in arvaukset:
                print(arvaus + ' on jo arvattu, arvaappa joku toinen')
                break
            else:
                arvaukset.append(arvaus)
                if arvaus in oikea:
                    print('Oikea arvaus!')
                    for i in range(len(oikea)):
                        if arvaus == oikea[i]:
                            tahtina = muutaKirjain(i, arvaus, tahtina)
                            break
                        else:
                            elamat -= 1
                            print('Väärä arvaus! menetit elämän')
                            break
        return tahtina, arvaukset, elamat

def muutaKirjain(i, arvaus, tahtina):
    listana = list(tahtina)
    listana[i] = str(arvaus)
    tahtina = ''.join(listana)
    return tahtina

def arvaaSana(oikea, arvaus):
    if oikea == arvaus:
        return True
    else:
        return False

def main():
    hirsiPuu(input('Syötä arvattava sana: '))

main()
