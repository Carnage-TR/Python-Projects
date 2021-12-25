##kullanıcı adı admin şifre 123456 girildiğinde başarılı giriş yazan bunun dışında herhangi biri veya ikisi yanlış olduğunda kullanıcı adı veya şifre hatalı yazan ve tekraqr kullanıcı adı ve şifre isteyen python programı yazınız.
while True:
    kullanici=input("kullanıcı adı gir").lower()
    sifre=input("şifre gir")
    if kullanici=="admin" and sifre=="123456":
        print("başarılı")
        print("sisteme girildi")
        break
    else:
        print("kullanıcı adı veya şifre hatalı")
