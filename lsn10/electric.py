from Perseritje import Kerri

class KerriElektrik(Kerri):
    def __init__(self,name,ngjyra,viti,baterija):
        super().__init__(name,ngjyra,viti)
        self.baterija = baterija

    def rriteShpejtesin(self):
        print("Shpejteisa nuk eshte duke u rritun")

