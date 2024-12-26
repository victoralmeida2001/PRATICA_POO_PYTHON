class Televisao:
    def __init__(self, canal, canal_min, canal_max):
        self.ligado = False
        self.canal = canal
        self.canal_min = canal_min
        self.canal_max = canal_max

        
    def escolher_canal(self):
        def __init__(self, canal, canal_min, canal_max):
            super().__init__(canal, canal_min, canal_max)
            self.canal_min = 2
            self.canal_max = 14
            print(f'O canal após ligado é = {self.canal}')

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1

    
tv = Televisao(13,)

tv.escolher_canal()

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)