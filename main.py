from StringMatching import *
from Greedy import * 

file = input("Masukkan nama file (tanpa extension): ")

print("----------------SELAMAT DATANG----------------")
countOrang = int(input("Masukkan berapa orang untuk rekomendasi menu ini: "))
inp = input("Apakah ada bahan yang ingin anda hindari? (y/n): ")
avoidIngredients = ""
countAvoid = 0
if (inp == 'y'):
    avoidIngredients = input("Apakah anda menghindari bahan tertentu? Silakan masukkan disini: ")
    countAvoid = int(input("Bahan ini dihindari untuk berapa orang? "))
print("Tentukan prioritas pemilihan menu untuk Anda")
print("1. Berdasarkan harga")
print("2. Berdasarkan rating")
print("3. Berdasarkan kalori")
print("4. Berdasarkan rating/harga")
print("5. Berdasarkan popularitas")
print("6. Berikan saya menu random")

listRecommendation = []
inp = int(input())
if (inp == 1):
    budget = int(input("Tentukan budget anda: "))
    listRecommendation, totalprice = greedyByPrice(file,budget,countOrang,avoidIngredients,countAvoid)
#elif (inp == 2):
#    listRecommendation = greedyByRating(file)
#elif (inp == 3):
#    listRecommendation = greedyByCalories(file)
#else:
#    listRecommendation = greedyByRatePerPrice(file)
print("Berikut ini adalah menu yang kami rekomendasikan berdasarkan masukan Anda")
print(listRecommendation)
print()
print(f"Dengan total harga {totalprice}")
if (len(listRecommendation) < countOrang):
    print("Maaf, dengan syarat yang anda berikan, kami belum bisa menampilkan rekomendasi agar semua orang dapat makanan")
