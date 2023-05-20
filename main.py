from StringMatching import *
from Greedy import * 
import sys
import random

file = input("Masukkan nama file (tanpa extension): ")
print()
print("----------------SELAMAT DATANG----------------")
run = True
while(run):
    print("Apakah Anda ingin membatasi jumlah menu yang ingin dipesan?")
    print("1. Ya, saya ingin membatasinya")
    print("2. Tidak, pesan sebanyak-banyaknya")
    inp = input()
    print()

    countOrang = 0
    if (inp == 1):
        countOrang = int(input("Masukkan berapa orang untuk rekomendasi menu ini: "))
    else:
        countOrang = sys.maxsize
    inp = input("Apakah ada bahan yang ingin anda hindari? (y/n): ")
    avoidIngredients = ""
    if (inp == 'y'):
        avoidIngredients = input("Apakah anda menghindari bahan tertentu? Silakan masukkan disini: ")
    print()
    max = 1
    inp = input("Apakah anda ingin semua menu berbeda? (y/n): ")
    if (inp == 'n'):
        max = int(input("Berapa maksimal kuantitas per menu yang anda inginkan? "))
    print()
    print("Tentukan prioritas pemilihan menu untuk Anda")
    print("1. Berdasarkan harga")
    print("2. Berdasarkan rating")
    print("3. Berdasarkan kalori")
    print("4. Berdasarkan popularitas")
    print("5. Berdasarkan semuanya")
    print("6. Berikan saya menu random")
    print()
    listRecommendation = []
    inp = int(input())
    budget = int(input("Tentukan budget anda: "))
    if (inp == 1):
        budget = int(input("Tentukan budget anda: "))
        listRecommendation, totalprice = greedyByPrice(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice}")
    elif (inp == 2):
        listRecommendation, totalprice, meanrating = greedyByRating(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice} dan rating rata-rata {meanrating}")
    elif (inp == 3):
        listRecommendation, totalprice, calories = greedyByCalories(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice} dan kalori total {calories}")
    elif (inp == 4):
        listRecommendation, totalprice = greedyByPopularity(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice}")
    elif (inp == 5):
        listRecommendation, totalprice, ratio = greedyByAll(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice} dan kalori total {ratio}")
    else:
        listRecommendation, totalprice = randomrecommendation(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice}")

    inp = input("Apakah Anda puas dengan rekomendasi ini? Jika tidak anda bisa mengulangnya (y/n): ")
    if (inp == 'n'):
        run = False

