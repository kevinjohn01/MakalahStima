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

def getBahan(filename):
    directory = os.getcwd() + "\\test\\" + filename + ".xlsx"
    column = ['Menu','Bahan']
    data_frame = pd.read_excel(directory,usecols=column)
    listbahan = data_frame.values
    return listbahan

def sortarray(array):
    x = np.array(array)
    sorted_array = x[x[:, 1].argsort()]
    return sorted_array
