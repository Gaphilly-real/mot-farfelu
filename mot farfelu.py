from random import choice
from prenoms import *
from verbecc import Conjugator
import csv

adj = []
adv = []
conjonc = []
deter = []
noms = []
pron = []
verbes = []
prenomsliste = []
conjugateur = Conjugator(lang="fr")

print('Les nouvelles du jour ')
prenomslistes= []
for i in range(0, 200000):
    prenomslistes.append(get_prenom())



file = open("noms.csv", "r", encoding='utf-8')
ns = list(csv.reader(file, delimiter="\n"))
file.close()


file = open("verbes.csv", "r", encoding='utf-8')
vs = list(csv.reader(file, delimiter="\n"))
file.close()

file = open("adj.csv", "r", encoding='utf-8')
adjs = list(csv.reader(file, delimiter="\n"))
file.close()

file = open("adv.csv", "r", encoding='utf-8')
advs = list(csv.reader(file, delimiter="\n"))
file.close()

file = open("conjonc.csv", "r", encoding='utf-8')
conjoncs = list(csv.reader(file, delimiter="\n"))
file.close()

file = open("deter.csv", "r", encoding='utf-8')
deters = list(csv.reader(file, delimiter="\n"))
file.close()

file = open("pronoms.csv", "r", encoding='utf-8')
pronoms = list(csv.reader(file, delimiter="\n"))
file.close()


def formater_liste_csv(listesrc, listedest, pronomstrue = False):
    for i in listesrc:
        if pronomstrue: 
            if i in pronoms :
                exec(listedest + ".append(i)")
        else:
            exec(listedest + ".append(i[0])")


for i in pronoms:
    for i in range(0, 2000):
        prenomslistes.append(i)

formater_liste_csv(vs, "verbes")
formater_liste_csv(ns, "noms")
formater_liste_csv(adjs, "adj")
formater_liste_csv(advs, "adv")
formater_liste_csv(conjoncs, "conjonc")
formater_liste_csv(deters, "deter")
formater_liste_csv(prenomslistes, "prenomsliste")


def generer_phrase():
    verbeinf = choice(verbes)
    prenom = choice(prenomsliste)
    nom = choice(noms)
    adje = choice(adj)
    adve = choice(adv)
    conjonct = choice(conjonc)
    determ = choice(deter)
    conjverbe = conjugateur.conjugate(verbeinf)
    conjugverb = ""
    verbeinf2 = choice(verbes)
    prenom2 = choice(prenomsliste)
    nom2 = choice(noms)
    adje2 = choice(adj)
    adve2 = choice(adv)
    conjonct2 = choice(conjonc)
    determ2 = choice(deter)
    conjverbe2 = conjugateur.conjugate(verbeinf2)
    conjugverb2 = ""
    temps = choice(["présent", "imparfait", "futur-simple", "passé-simple", "passé-composé", "plus-que-parfait", "futur-antérieur", "passé-antérieur"])
    if (prenom != "je"and prenom != "tu" and prenom != "il" and prenom != "elle" and prenom != "on") and (prenom != "nous" and prenom != "vous" and prenom != "ils" and prenom != "elles"):
        conjugverbs = conjverbe['moods']['indicatif'][temps][2]
        conjugverb = conjugverbs.replace("il", prenom)
        conjugverbs2 = conjverbe2['moods']['indicatif'][temps][2]
        conjugverb2 = conjugverbs2.replace("il", prenom2)
    elif prenom == "je":
        conjugverb = conjverbe['moods']['indicatif'][temps][0]
        conjugverb2 = conjverbe2['moods']['indicatif'][temps][0]
    elif prenom == "tu":
        conjugverb = conjverbe['moods']['indicatif'][temps][1]
        conjugverb2 = conjverbe2['moods']['indicatif'][temps][1]
    elif prenom == "il" or prenom == "elle" or prenom == "on":
        conjugverb = conjverbe['moods']['indicatif'][temps][2]
        conjugverb2 = conjverbe2['moods']['indicatif'][temps][2]
    elif prenom == "nous":
        conjugverb = conjverbe['moods']['indicatif'][temps][3]
        conjugverb2 = conjverbe2['moods']['indicatif'][temps][3]
    elif prenom == "vous":
        conjugverb = conjverbe['moods']['indicatif'][temps][4]
        conjugverb2 = conjverbe2['moods']['indicatif'][temps][4]
    elif prenom == "ils":
        conjugverb = conjverbe['moods']['indicatif'][temps][5]
        conjugverb2 = conjverbe2['moods']['indicatif'][temps][5]
    phrase = conjugverb + " " + determ + " " + nom + " " + conjonct + " " + conjugverb2 + " "+ determ2 + " " + nom2 + "."
    print(phrase)
while True:
    for i in range(0,30):
        try:
            generer_phrase()
        except:
            pass
    input()