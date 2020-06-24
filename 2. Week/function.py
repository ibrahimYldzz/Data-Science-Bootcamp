#2 string metodu, 2 liste metodu ve 1 döngü
#işlemin sonucu return

#çok mantıklı bir fonksiyon olmasada ödev kurallarına uygun return eden bir fonksiyon

def fonksiyon():
   liste = ["ibrahim","ali","veli","ayşe","mehmet"]
   notlar = [100,75,50,60,0]
   liste_copy = liste.copy() #list method
   
   for i in range(0,len(liste)):
       a = liste_copy[i]
       a.capitalize() #string method
       liste_copy.append(notlar[i]) #list method
   
   liste_copy[3].replace("şe","ça") #string method
   
   toplam = 0
   for i in notlar:
       toplam = toplam + i
       
   return toplam    
       
ortalama = fonksiyon() / 5

print(ortalama)      
 