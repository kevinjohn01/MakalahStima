import pandas as pd
import os
import numpy as np

def importfile(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    data_frame = pd.read_excel(directory)
    listmenu = data_frame.values
    return listmenu

def getPrice(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Harga']
    data_frame = pd.read_excel(directory,usecols=column)
    listprice = data_frame.values
    return listprice

def getRating(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Rating']
    data_frame = pd.read_excel(directory,usecols=column)
    listrating = data_frame.values
    return listrating

def getCalories(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Kalori']
    data_frame = pd.read_excel(directory,usecols=column)
    listcalories = data_frame.values
    return listcalories

def getTerjual(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Terjual']
    data_frame = pd.read_excel(directory,usecols=column)
    listterjual = data_frame.values
    return listterjual

def getBahan(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Bahan']
    data_frame = pd.read_excel(directory,usecols=column)
    listbahan = data_frame.values
    return listbahan

def getPopularity(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Terjual']
    data_frame = pd.read_excel(directory,usecols=column)
    listorigin = data_frame.values

    return listorigin

def getAll(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Harga','Rating','Terjual']
    data_frame = pd.read_excel(directory,usecols=column)
    listorigin = data_frame.values

    listresult= np.empty((0,2))
    for i in range(0,len(listorigin)):
        # Kolom ketiga: harga, kolom keempat: rating, kolom kelima: Jumlah terjual
        ratio = float(listorigin[i][2])*float(listorigin[i][3])/float(listorigin[i][1])
        array = np.array([listorigin[i][0],ratio])
        listresult = np.append(listresult,[array],axis=0)
    return listresult

def sortarrayasc(array):
    x = np.array(array)
    sorted_array = x[x[:, 1].argsort()]
    return sorted_array

def sortarraydesc(array):
    x = np.array(array)
    sorted_array = x[x[:, 1].argsort()[::-1]]
    return sorted_array