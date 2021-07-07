# -*-coding:Utf-8 -*
print("hello")

# 1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche “positif” ou “négatif”.

# n = input("Donnez moi un entier")
# n = int(n)
# if n>= 0:
# print("positif")
# else:
# print("négatif")


# 2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictementnégatif, et affiche ce résultat.

# j = input("utilisateur donnez moi un entier svp")
# j = int(j)
# if j>0:
# print("strictement positif")
# elif j==0:
# print("nul")
# else:
# print("strictement négatif")

# 3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction prédéfinie évidemment).

# k = input("utilisateur donnez moi un réel please")
# k = float(k)
# if k >= 0:
#   print("la valeur absolue est", k)
# else:
#   print("la valeur absolue est", -k)


# 4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis à l’entier supérieur).

# l = input("utilsateur pouvez vous me donner un réel svp")
# l = float(l)
# print(round(l))

#2epossibilite

#i_reel = input("rentrez un entier")
#i_reel = float(i_reel)
#i_tronque = int(i_reel)
#delta = i_reel - i_tronque
#i_arrondi = i_tronque
#if delta >= 0.5 and i_reel >=0:
    #i_arrondi = i_tronque + 1
#elif delta >=0.5 and i_reel <0:
#i_arrondi = i_tronque - 1
#print(i_arrondi)


# 5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir compte des années bissextiles).

# m = input("donnez moi le numéro d'un mois")
# m = int(m)
# if m in [4,6,9,11]:
#     print("30")
# elif m in [1,3,5,7,8,10,12]:
#     print("31")
# else:
#     print("29")

# 6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les 4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans (2000 était une année bissextile).

# Pour être bissextile une année doit être divisible par 4,100 et 400. Si une année est divisible par 4 mais pas par 100 elle est bissextile.

# annee = input("Entrez l'année à verifier")
# annee = int(annee)
# if(annee%4==0 and annee%100!=0) or annee%400==0:
#     print("l'année est bissextile")
# else:
#     print("l'année n'est pas bissextile")

# 7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois) et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.

jour = input("entrez un jour")
mois = input("entrez un mois")
jour = int(jour)
mois = int(mois)
if (mois == 12 and jour > 21) or mois == 1 or mois == 2 or (mois == 3 and jour < 21):
    print("c'est l'hiver")
elif (mois == 3 and jour > 21) or mois == 4 or mois == 5 or (mois == 6 and jour < 21):
    print("c'est le printemps")
elif (mois == 6 and jour > 21) or mois == 7 or mois == 8 or (mois == 9 and jour < 21):
    print("c'est l'été")
else:
    print("c'est l'automne")
