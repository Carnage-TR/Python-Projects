list=[]
while True:
    for i in range(10):
        sayi=int(input("sayı gir"))
        list.append(sayi)
    soru=input("küçükten büyüye mi sıralamak istersin yokse büyükten küçüğe sıralamak mı?")
    if soru=="büyükten küçüğe":
        list.sort(reverse=True)
        print(list)
    elif soru=="küçükten büyüğe":
        list.sort(reverse=False)
        print(list)
    else:
        print("knk geçersiz işlem girdin:(")
        continue
