#kukllanıcı negatif sayı girdikçe kabul etmeyip tekrar ekrana sayı giriniz yazarak sayı girilmesini isteyen python programı

sayi=int(input("sayı giriniz"))

while sayi <=0:
    print("negatif sayı yazma!")
    sayi=int(input("sayı giriniz"))
