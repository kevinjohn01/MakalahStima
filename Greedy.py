from filemgm import *
from StringMatching import *
import random

def getBahanByMenu(listbahan,namamenu):
    for i in range(0,len(listbahan)):
        if (listbahan[i][0] == namamenu):
            return listbahan[i][1]
    return -1

def greedyByPrice(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listprice = getPrice(filename)
    listbahan = getBahan(filename)
    totalprice = 0
    maxnow = max

    listpricesort = sortarrayasc(listprice)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listpricesort[i][0]
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalprice += listpricesort[i][1]
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
        
        if (i>len(listpricesort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= listpricesort[i][1]
        result = removeLastElement(result)
    return result, totalprice

def greedyByRating(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listrating = getRating(filename)
    listbahan = getBahan(filename)
    listprice = getPrice(filename)
    totalprice = 0
    meanrating = 0
    maxnow = max

    listratingsort = sortarraydesc(listrating)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listratingsort[i][0]
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                meanrating = (meanrating*(len(result)-1)+listratingsort[i][1])/(len(result))
                totalprice += getPriceByMenu(listprice,menu)
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
        
        if (i>len(listratingsort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice, meanrating

def greedyByCalories(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listcalories = getCalories(filename)
    listbahan = getBahan(filename)
    listprice = getPrice(filename)
    totalprice = 0
    totalcalories = 0
    maxnow = max

    listcaloriessort = sortarrayasc(listcalories)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listcaloriessort[i][0]
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalcalories += listcaloriessort[i][1]
                totalprice += getPriceByMenu(listprice,menu)
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
        
        if (i>len(listcaloriessort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice, totalcalories

def greedyByPopularity(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listpopularity = getPopularity(filename)
    listbahan = getBahan(filename)
    listprice = getPrice(filename)
    totalprice = 0
    maxnow = max

    listpopsort = sortarraydesc(listpopularity)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listpopsort[i][0]
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalprice += getPriceByMenu(listprice,menu)
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
        
        if (i>len(listpopsort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice

def greedyByAll(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listratio = getAll(filename)
    listbahan = getBahan(filename)
    listprice = getPrice(filename)
    totalprice = 0
    totalratio = 0
    maxnow = max

    listratiosort = sortarraydesc(listratio)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listratiosort[i][0]
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalratio += float(listratiosort[i][1])
                totalprice += getPriceByMenu(listprice,menu)
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
        
        if (i>len(listratiosort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice, totalratio

def randomrecommendation(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listbahan = getBahan(filename)
    listprice = getPrice(filename)
    totalprice = 0
    maxnow = max

    while(totalparticipant > 0 and totalprice < budget):
        x = random.randint(0,len(listprice)-1)
        menu = listprice[x][0]
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalprice += getPriceByMenu(listprice,menu)
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice

        
def fungsikendala(avoidIngredients,bahan):
    arrayAvoid = avoidIngredients.split()
    avoid = False
    for avoid in arrayAvoid:
        if (boyermoore(bahan,avoid) == -1):
            avoid = False
        else:
            avoid = True
            break
    return avoid

def addMenu(listRecommendation,menu):
    found = False
    if (len(listRecommendation) != 0):
        for i in (0,len(listRecommendation)-1):
            if (listRecommendation[i,0] == menu):
                listRecommendation[i,1] = int(listRecommendation[i,1]) + 1
                found = True
                break
    if (found == False):
        array = np.array([menu,1])
        listRecommendation = np.append(listRecommendation,[array],axis=0)
    return listRecommendation

def printMenu(listRecommendation):
    print("  Menu - Quantity")
    for i in range (0,len(listRecommendation)):
        print(f"{i+1}. {listRecommendation[i][0]} - {listRecommendation[i][1]}")

def removeLastElement(listRecommendation):
    i = len(listRecommendation)-1
    if (int(listRecommendation[i,1]) >1):
        listRecommendation[i,1] = int(listRecommendation[i,1]) -1
    else:
        listRecommendation = listRecommendation[:-1]
    return listRecommendation

def getPriceByMenu(listprice,menu):
    for i in range (0,len(listprice)-1):
        if (listprice[i][0]==menu):
            return listprice[i][1]
    return -1
