def getKeyByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    keys = ''.join(listOfKeys)
    return  keys


def DNAtest(file):
    global counter
    with open(file) as input_file:
        dna = input_file.read()
        #print(dna)
        for lastnost in Lastnosti: #Lastnost je slovar 
            lastnost_tip = lastnost.values() #Dobim seznam vrednosti (values)
            for tip in lastnost_tip: #Tip je vsaka vrednost v seznamu vrednosti
                if tip in dna: #Preverimo, ce je tip v dna
                    kljuc = getKeyByValue(lastnost, tip) #Dobim pravi tip lastnosti
                    if counter == 0:
                        barva_las = kljuc
                    elif counter == 1:
                        oblika_obraza = kljuc
                    elif counter == 2:
                        barva_oci = kljuc
                    elif counter == 3:
                        spol = kljuc
                    else:
                        rasa = kljuc
                    counter = counter + 1
                
        print("Gender: "+spol)
        print("Race: "+rasa)
        print("Hair color: "+barva_las)
        print("Eye color: "+barva_oci)
        print("Face shape: "+oblika_obraza)

        #V Rezultat dodamo dobljene vrednosti
        Rezultat["Gender"] = spol
        Rezultat["Race"] = rasa
        Rezultat["Hair color"] = barva_las
        Rezultat["Eye color"] = barva_oci
        Rezultat["Face shape"] = oblika_obraza

        print()

        counter = 0 #Sedaj je ta stevec za ugotaljanje imena osumljenca
        for oseba in Osumljenci: #Gremo skozi vse osumljnce in preverjamo njihove lastnosti z dobljenim rezultatom
            if oseba == Rezultat:
                if counter == 0:
                    print("Sladoled je pojedla Eva")
                elif counter == 1:
                    print("Sladoled je pojedla Larisa")
                elif counter == 2:
                    print("Sladoled je pojedel Matej")
                else:
                    print("Sladoled je pojedel Miha")
            counter = counter + 1

if __name__ == "__main__":
    Lastnosti = []
    hair_color = {"Black": "CCAGCAATCGC", "Brown": "GCCAGTGCCG", "Blonde": "TTAGCTATCGC"}
    facial_shape = {"Square": "GCCACGG", "Round": "ACCACAA", "Oval": "AGGCCTCA"}
    eye_color = {"Blue": "TTGTGGTGGC", "Green": "GGGAGGTGGC", "Brown": "AAGTAGTGAC"}
    gender = {"Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC"}
    race ={"White": "AAAACCTCA", "Black": "CGACTACAG", "Asian": "CGCGGGCCG"}

    Lastnosti.append(hair_color)
    Lastnosti.append(facial_shape)
    Lastnosti.append(eye_color)
    Lastnosti.append(gender)
    Lastnosti.append(race)

    barva_las = ""
    oblika_obraza = ""
    barva_oci = ""
    spol = ""
    rasa = ""

    counter = 0

    Osumljenci = []
    Eva = {"Gender": "Female", "Race": "White", "Hair color": "Blonde", "Eye color": "Blue", "Face shape": "Oval"}
    Larisa = {"Gender": "Female", "Race": "White", "Hair color": "Brown", "Eye color": "Brown", "Face shape": "Oval"}
    Matej = {"Gender": "Male", "Race": "White", "Hair color": "Black", "Eye color": "Blue", "Face shape": "Oval"}
    Miha = {"Gender": "Male", "Race": "White", "Hair color": "Brown", "Eye color": "Green", "Face shape": "Square"}

    Osumljenci.append(Eva)
    Osumljenci.append(Larisa)
    Osumljenci.append(Matej)
    Osumljenci.append(Miha)

    Rezultat = {}

    DNAtest("dna.txt")