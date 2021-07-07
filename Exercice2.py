# -*-coding:Utf-8 -*
print("hello")

#1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.

# i = -1
# while (i < 0):
#     i = int(float(input("veuillez saisir un entier positif")))
#     if i < 0:
#         print("le nombre", i, "est négatif, reessayez")
# print("le nombre saisi est positif")

#2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.

# somme = 0
# for i in range(10):
#     a = int(float(input("saisir entier positif ou negatif")))
#     if a >= 0:
#         somme = somme + 1
# print("le nbr d'entiers positifs est", somme)

#3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le résultat dès qu’un entier négatif est saisi.

# i = 1
# somme = 0
# while i >= 0:
#     i = int(float(input("rentrez un entier positif")))
#     if i >= 0:
#         somme = somme + i
# print("la somme des entiers postifis est egale à", somme)


#4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.

i = 1
somme = 0
while i >= 0:
    i = int(float(input("rentrez un entier positif")))
    if i >= 0:
        somme = (somme + i) / i
print("la moyenne des entiers postifis est egale à", somme)
