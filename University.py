class okul():
    tip = "egitimyeri"

    def __init__(self, adi, turu,calisan_sayisi, ogretmen_sayisi, ögrenci_sayisi, sinif_sayisi,ders_sayisi):
        self.adi = adi
        self.turu = turu
        self.calisan_sayisi=calisan_sayisi
        self.ogretmen_sayisi = ogretmen_sayisi
        self.ögrenci_sayisi = ögrenci_sayisi
        self.sinif_sayisi = sinif_sayisi
        self.ders_sayisi=ders_sayisi

Universite1 = okul("Hasan Kalyoncu", "Üniversitesi",1100, 600,1500,100,200)
Universite2 = okul("GAZI", "Üniversitesi", 1000,500 , 2000,100,190)
Universite3 = okul("GAUN", "Üniversitesi", 2000, 1100,3300, 1200,990)

Okullar = [Universite1,Universite2,Universite3]

for Okul in Okullar:
    
    print(Okul.adi, Okul.turu,Okul.calisan_sayisi, Okul.ogretmen_sayisi, Okul.ögrenci_sayisi, Okul.sinif_sayisi, Okul.ders_sayisi)

