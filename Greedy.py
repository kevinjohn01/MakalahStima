from filemgm import *
from StringMatching import *

def getBahanByMenu(listbahan,namamenu):
    for i in range(0,len(listbahan)):
        if (listbahan[i][0] == namamenu):
            return listbahan[i][0]
    return -1

def greedyByPrice(filename, budget, totalparticipant, listAvoidIngredient, countavoid, max):
    result = np.array([])
    listprice = getPrice(filename)
    listbahan = getBahan(filename)
    totalprice = 0

    listpricesort = sortarray(listprice)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listpricesort[i][0]
        print(f"cek {menu}")
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = np.append(result,menu)
                totalparticipant -= 1
                totalprice += listpricesort[i][1]
                print(f"{menu} berhasil ditambahkan")
            else:
                countavoid -= 1
                print(f"{menu} mengandung bahan yang tak diinginkan")
        
        i += 1
        if (i>len(listpricesort)-1):
            i = 0
    return result, totalprice
        
def fungsikendala(avoidIngredients,bahan):
    arrayAvoid = avoidIngredients.split()
    print(arrayAvoid)
    avoid = False
    for avoid in arrayAvoid:
        print(boyermoore(bahan,avoid))
        if (boyermoore(bahan,avoid) == -1):
            avoid = False
        else:
            avoid = True
            break
    print(avoid)
    return avoid
