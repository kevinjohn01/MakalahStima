from filemgm import *
from StringMatching import *

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
        #print(f"cek {menu}")
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalprice += listpricesort[i][1]
                #print(f"{menu} berhasil ditambahkan")
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
                #print(f"{menu} mengandung bahan yang tak diinginkan")
        
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
    print(listratingsort)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listratingsort[i][0]
        #print(f"cek {menu}")
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                meanrating = (meanrating*(len(result)-1)+listratingsort[i][1])/(len(result))
                totalprice += getPriceByMenu(listprice,menu)
                #print(f"{menu} berhasil ditambahkan")
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
                #print(f"{menu} mengandung bahan yang tak diinginkan")
        
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
    #print(listcaloriessort)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listcaloriessort[i][0]
        #print(f"cek {menu}")
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalcalories += listcaloriessort[i][1]
                totalprice += getPriceByMenu(listprice,menu)
                #print(f"{menu} berhasil ditambahkan")
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
                #print(f"{menu} mengandung bahan yang tak diinginkan")
        
        if (i>len(listcaloriessort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice, totalcalories

def greedyByRatingPerPrice(filename, budget, totalparticipant, listAvoidIngredient,max):
    result = np.empty((0,2))
    listratio = getRatingPerPrice(filename)
    listbahan = getBahan(filename)
    listprice = getPrice(filename)
    totalprice = 0
    totalratio = 0
    maxnow = max

    listratiosort = sortarraydesc(listratio)
    print(listratiosort)
    #print(listcaloriessort)
    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listratiosort[i][0]
        #print(f"cek {menu}")
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalratio += float(listratiosort[i][1])
                totalprice += getPriceByMenu(listprice,menu)
                #print(f"{menu} berhasil ditambahkan")
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
                #print(f"{menu} mengandung bahan yang tak diinginkan")
        
        if (i>len(listratiosort)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice, totalratio

def randomrecommendation(filename, listAvoidIngredient, budget, max):
    result = np.empty((0,2))
    listbahan = getBahan(filename)
    listprice = getPrice(filename)

    i = 0
    while(totalparticipant > 0 and totalprice < budget):
        menu = listprice[i][0]
        #print(f"cek {menu}")
        bahan = getBahanByMenu(listbahan,menu)
        if (bahan != -1):
            if (fungsikendala(listAvoidIngredient,bahan) == False):
                result = addMenu(result,menu)
                totalparticipant -= 1
                totalprice += getPriceByMenu(listprice,menu)
                #print(f"{menu} berhasil ditambahkan")
                maxnow -=1
                if (maxnow == 0):
                    maxnow = max
                    i += 1
            else:
                i += 1
                #print(f"{menu} mengandung bahan yang tak diinginkan")
        
        if (i>len(listprice)-1):
            i = 0
    if (totalprice > budget):
        totalprice -= getPriceByMenu(listprice,menu)
        result = removeLastElement(result)  
    return result, totalprice

        
def fungsikendala(avoidIngredients,bahan):
    #print(bahan)
    arrayAvoid = avoidIngredients.split()
    #print(arrayAvoid)
    avoid = False
    for avoid in arrayAvoid:
        #print(avoid)
        #print(boyermoore(bahan,avoid))
        if (boyermoore(bahan,avoid) == -1):
            avoid = False
        else:
            avoid = True
            break
    #print(avoid)
    return avoid

def addMenu(listRecommendation,menu):
    found = False
    #print(listRecommendation)
    if (len(listRecommendation) != 0):
        for i in (0,len(listRecommendation)-1):
            #print(listRecommendation[i,0])
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
