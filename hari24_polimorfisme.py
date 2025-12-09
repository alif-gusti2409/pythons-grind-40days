class hewan:
    def suara(self):
        pass

class anjing(hewan):
    def suara(self):
        print("Guk")

class kucing(hewan):
    def suara(self):
        print("Meong")

class sapi(hewan):
    def suara(self):
        print("Moo")

class ayam(hewan):
    def suara(self):
        print("Petok")

hewan = [anjing(), kucing(), sapi(), ayam()]
for h in hewan:
    h.suara()