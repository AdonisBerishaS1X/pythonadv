from perseritje import Kerri


class KerriE(Kerri):
    def __init__(self,name,viti,gjendja,ngjyra,bateria):
        super().__init__(name,viti,gjendja,ngjyra)
        self.bateria = bateria



    def musheBaterin(self):
        print("bateria eshte duke u mbushur")
