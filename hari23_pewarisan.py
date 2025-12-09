class pegawai:
    def __init__(self, nama):
     self.nama = nama

    def info(self):
        print("nama:", self.nama)

class manajer(pegawai):
        def __init__(self, nama, devisi):
            super().__init__(nama)
            self.devisi = devisi

        def info(self):
         super().info()
         print("devisi:", self.devisi)

class staf(pegawai):
    def __init__(self, nama, shift):
        super().__init__(nama)
        self.shift = shift

    def info(self):
        super().info()
        print("shift:", self.shift)

m = manajer("Andi", "Keuangan")
m.info()

s = staf("Budi", "Malam")
s.info()