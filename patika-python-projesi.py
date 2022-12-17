
# Bir listeyi düzleştiren flatten fonksiyon

def flatten(lst):
    duz_liste = []
    for element in lst:
        if isinstance(element, list):
            duz_liste.extend(flatten(element))
        else:
            duz_liste.append(element)
    return duz_liste

Liste = [[1, 2, [3, 4]], [5, 6], 7]
print(flatten(Liste))   # output = [1, 2, 3, 4, 5, 6, 7]



#  listedeki elemanlari tersine cevirme

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste.reverse()
print(liste)    # [5, 4, [[[3]], 'dog'], [1, 'a', ['cat'], 2]]







