#4 matematiksel işlem için 4 ayrı fonksiyon yazınız.
#toplama:1, çıkarma:2, çarpma:3, bölme:4
#if ile kullanıcıdan alınan bilgiye göre tasarla.

def topla():
    x = int(input("İlk sayi:"))
    y = int(input("İkinci sayi:"))
    print("Sonuc: ",x+y)

def cikar():
    x = int(input("İlk sayi:"))
    y = int(input("İkinci sayi:"))
    print("Sonuc: ",x-y)

def carp():
    x = int(input("İlk sayi:"))
    y = int(input("İkinci sayi:"))
    print("Sonuc: ",x*y)

def bol():
    x = int(input("İlk sayi:"))
    y = int(input("İkinci sayi:"))
    print("Sonuc: ",x/y)

def calculator():
    print("1-Toplama")
    print("2-Cıkarma")
    print("3-Carpma")
    print("4-Bolme")
    
    info = int(input("Lutfen yapmak istediginiz islemi seciniz:"))

    if info==1:
        topla()        
    elif info==2:
        cikar()
    elif info==3:
        carp() 
    elif info==4:
        bol()   
    else:
        print("Hatali tuslama")    
        calculator()

calculator()

        