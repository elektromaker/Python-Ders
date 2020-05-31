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

    def enduktans(self):
        return math.sqrt(self.R**2 + (kapReaktans-endReaktans)**2)

    def akim(self):
        return (self.V/Enduktans)*1000

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
Enduktans = hesapla.enduktans()
Akim = hesapla.akim()
DirencVolt = hesapla.direncGerilimi()
BobinVolt = hesapla.bobinGerilimi()
KondansatorVolt = hesapla.kondansatorGerilim()
FazAci = hesapla.fazAcisi()
print("Endüktif Reaktans: " + str(round(endReaktans,2)) + " ohm")
print("Kapasitif Reaktans: " + str(round(kapReaktans,2)) + " ohm")
print("Endüktans: " + str(round(Enduktans,2)) + " ohm")
print("Akım(miliAmper): " + str(round(Akim,2)) + " mA")
print("Direnç üzerine düşen gerilim: " + str(round(DirencVolt,2)) + " V")
print("Bobin üzerine düşen gerilim: " + str(round(BobinVolt,2)) + " V")
print("Kondansatör üzerine düşen gerilim: " + str(round(KondansatorVolt,2)) + " V")
print("Faz açısı: " + str(round(FazAci,2)) + " Derece")