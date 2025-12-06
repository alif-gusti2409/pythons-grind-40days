class AkunBank:
    def __init__(self, nama, saldo):
        self._nama = nama
        self.__saldo = saldo 

    def setor(self, jumlah):
        self.__saldo += jumlah
        
    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")
    
    def get_saldo(self):
        return self.__saldo
    
a = AkunBank("Budi", 1000000)
a.setor(500000)
a.tarik(2000)
print("saldo sekranga: ", a.get_saldo())


