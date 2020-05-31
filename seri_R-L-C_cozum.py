####################################
#Yazar: Elekktromaker.com
#Açıklama:
#Bu kod Meslek lisesindeki elektrik-elektronik esasları dersindeki Seri RLC develer konusu için hazırlanmıştır.
#İdeal bobin ve ideal kondansatör kullanılan (akım ve gerilim arasında doksan derece faz farkı bulunan elemanlar)
#seri RLC devrelerinde; Direnç, bobin, kondansatör, Frekans ve gerilim değerleri verilerek;
#Endüktif reaktans, kapasitif reaktans, Empedans, Akım, Elemanlar üzerine düşen gerilimler ve faz açısının hesaplanmasını yapan
#python kodarıdır.
##################################### 
import math
class SeriRLC:
    
    def __init__(self):
        self.R = float(input("Direnç değeri giriniz(ohm):"))
        self.L = float(input("Bobin değeri giriniz(miliHenry):"))
        self.C = float(input("Kondansatör değeri giriniz(mikroFarad):"))
        self.f = float(input("Frekans değeri giriniz(Hz):"))
        self.V = float(input("Kaynak gerilimi değerini giriniz(Volt):"))

    def enduktifReaktans(self):
        return 2*3.14*self.f*self.L*10**(-3)

    def kapasitifReaktans(self):
        return 10**(6)/(2*3.14*60*self.C)

    def empedans(self):
        return math.sqrt(self.R**2 + (kapReaktans-endReaktans)**2)

    def akim(self):
        return (self.V/Empedans)*1000

    def direncGerilimi(self):
        return (Akim/1000)*self.R

    def bobinGerilimi(self):
        return (Akim/1000)*endReaktans

    def kondansatorGerilim(self):
        return (Akim/1000)*kapReaktans

    def fazAcisi(self):
        return math.degrees(math.atan((kapReaktans-endReaktans)/self.R))

hesapla = SeriRLC()
endReaktans = hesapla.enduktifReaktans()
kapReaktans = hesapla.kapasitifReaktans()
Empedans = hesapla.empedans()
Akim = hesapla.akim()
DirencVolt = hesapla.direncGerilimi()
BobinVolt = hesapla.bobinGerilimi()
KondansatorVolt = hesapla.kondansatorGerilim()
FazAci = hesapla.fazAcisi()
print("Endüktif Reaktans: " + str(round(endReaktans,2)) + " ohm")
print("Kapasitif Reaktans: " + str(round(kapReaktans,2)) + " ohm")
print("Empedans: " + str(round(Empedans,2)) + " ohm")
print("Akım(miliAmper): " + str(round(Akim,2)) + " mA")
print("Direnç üzerine düşen gerilim: " + str(round(DirencVolt,2)) + " V")
print("Bobin üzerine düşen gerilim: " + str(round(BobinVolt,2)) + " V")
print("Kondansatör üzerine düşen gerilim: " + str(round(KondansatorVolt,2)) + " V")
print("Faz açısı: " + str(round(FazAci,2)) + " Derece")
