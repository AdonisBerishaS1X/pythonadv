class Kafsha():
    def __init__(self,emri):
        self.emri=emri

    def tingulli(self):
        print("Kafsha ben nje tingull")


class Maca(Kafsha):

    def tingulli(self):
        print("Kafsha ben nje tingull")


class Qeni(Kafsha):

    def tingulli(self):
        print("HAM HAM")

kafsha1 = Kafsha("Csahdkj")
kafsha1.tingulli()

qeni = Qeni("Booby")
qeni.tingulli()

maca = Maca("Meow")
maca.tingulli()