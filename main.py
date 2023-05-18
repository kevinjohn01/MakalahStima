from StringMatching import *
from Greedy import * 

file = input("Masukkan nama file (tanpa extension): ")

print("----------------SELAMAT DATANG----------------")
run = True
while(run):
    countOrang = int(input("Masukkan berapa orang untuk rekomendasi menu ini: "))
    inp = input("Apakah ada bahan yang ingin anda hindari? (y/n): ")
    avoidIngredients = ""
    #countAvoid = 0
    if (inp == 'y'):
        avoidIngredients = input("Apakah anda menghindari bahan tertentu? Silakan masukkan disini: ")
        #countAvoid = int(input("Bahan ini dihindari untuk berapa orang? "))
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
    print("4. Berdasarkan rating/harga")
    print("5. Berdasarkan popularitas")
    print("6. Berdasarkan popularitas*rating")
    print("6. Berikan saya menu random")
    print()
    listRecommendation = []
    inp = int(input())
    if (inp == 1):
        budget = int(input("Tentukan budget anda: "))
        listRecommendation, totalprice = greedyByPrice(file,budget,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {totalprice}")
    elif (inp == 2):
        listRecommendation, meanrating = greedyByRating(file,countOrang,avoidIngredients,max)
        print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
        printMenu(listRecommendation)
        print()
        print(f"Dengan total harga {meanrating}")
    #elif (inp == 3):
    #    listRecommendation = greedyByCalories(file)
    #else:
    #    listRecommendation = greedyByRatePerPrice(file)
    inp = input("Apakah Anda puas dengan rekomendasi ini? Jika tidak anda bisa mengulangnya (y/n): ")
    if (inp == 'n'):
        run = False

