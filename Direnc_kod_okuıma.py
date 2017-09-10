#-*- coding: utf-8-*-
print("""**********************
Direnç değeri okuma programı
**********************      
""")
direnc =[]
deger = {'siyah':0, 'kahve':1, 'kırmızı':2, 'turuncu':3, 'sarı':4, 'yeşil':5, 'mavi':6, 'mor':7, 'gri':8, 'beyaz':9}
carpan = {'siyah':1, 'kahve':10, 'kırmızı':10**2, 'turuncu':10**3, 'sarı':10**4, 'yeşil':10**5, 'mavi':10**6, 'mor':10**7, 'gri':10**8, 'beyaz':10**9}
tolerans = {'kahve':'%1', 'kırmızı':'%2', 'yeşil':'%0.5', 'mavi':'%0.25', 'mor':'%0.1', 'gri':'%0.05', 'altın':'%5', 'gümüş':'%10'}
for i in range(1,5):
    giris = input("{}. renk değerini giriniz: ".format(i))
    #print(deger[giris])
    if i <= 2 :
        direnc.append(deger[giris])
    elif i == 3 :
        direnc.append(carpan[giris])
    else:
        direnc.append(tolerans[giris])
print(direnc)
ohm = ((direnc[0])*10 + direnc[1])*direnc[2]
if ohm >= 1000:
    ohm = int(ohm/1000)
    print("Direnc değeri", ohm, "kohm tolerans", direnc[3])
else:
    print("Direnc değeri",ohm , "ohm tolerans", direnc[3])
#print(deger)
#print(carpan)
