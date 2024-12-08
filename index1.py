from itertools import product
def nombre_de_fois_20():
    total=0
    for combinaison in product(range(1,7),repeat=5):
        if sum(combinaison) == 20:
            total += 1
    return total  
print("Nombre de façon d'obtenir 20 est :",nombre_de_fois_20())  