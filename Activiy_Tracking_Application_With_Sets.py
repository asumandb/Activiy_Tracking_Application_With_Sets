class Aktivite_Takip:
     
    def __init__(self):
        self.aktiviteler = set()

    def aktivite_ekle(self, aktivite):
        self.aktiviteler.add(aktivite)
        print(f"'{aktivite}' aktivitesi eklendi.  ")

    def aktiviteleri_goruntule(self):
        if self.aktiviteler:
            print(f"Bügünkü aktiviteler:")
            for aktivite in self.aktiviteler:
                print(aktivite)

        else:
            print(f"Henüz eklenmiş bir aktivite yok.")

takip = Aktivite_Takip()
takip.aktivite_ekle("Kitap Okuma")
takip.aktivite_ekle("Ödev Yapma")
takip.aktivite_ekle("Müzik Dinleme")
takip.aktiviteleri_goruntule()
