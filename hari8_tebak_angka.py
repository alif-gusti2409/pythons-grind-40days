import random

print("game tebak angka")
angka_rahasia = random.randint(1, 20)
percobaan = 0

while True:
    tebakan = int(input("tebak angka (1-20):  "))
    percobaan += 1
    tebakan<4
    score = 10
    if tebakan == angka_rahasia:
        print(f"benar! kamu menebak dalam {percobaan} kali percobaan kamu mendapat 10")
        break
    elif tebakan < angka_rahasia:
         print("terlau kecil ")
    else:
         print("telau besar ")
    
    if tebakan == angka_rahasia:
     print(f"kamu mendapat {score + 10 }")
     break
    else:
        print(f"skormu {score - 5}")


    


