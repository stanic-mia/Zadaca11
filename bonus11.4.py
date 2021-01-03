# CSI forensics program

hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
face = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eyes = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

people = {"eva": ["blonde", "oval", "blue", "female", "white"],
          "larisa": ["brown", "oval", "brown", "female", "white"],
          "matej": ["black", "oval", "blue", "male", "white"],
          "miha": ["brown", "square", "green", "male", "white"]}

with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

suspect = []

print("Characteristics of the suspect: ")

# provjera boje kose
for x in hair:
    if hair[x] in dna:
        print("hair: " + x)
        suspect.append(x)

# provjera oblika lica
for x in face:
    if face[x] in dna:
        print("face: " + x)
        suspect.append(x)

# provjera boje očiju
for x in eyes:
    if eyes[x] in dna:
        print("eyes: " + x)
        suspect.append(x)

# provjera spola
for x in gender:
    if gender[x] in dna:
        print("gender: " + x)
        suspect.append(x)

# provjera rase
for x in race:
    if race[x] in dna:
        print("race: " + x)
        suspect.append(x)

for person in people:
    if people[person] == suspect:
        print("The suspect is {}".format(person.capitalize()))
        break



