# 다형성(Polymorphism)

class ArmorSuite:
    def armor(self):
        print('armored.')

class IronMan(ArmorSuite):
    pass


def get_armored(suite):
    suite.armor()



if __name__ == '__main__':
    a = ArmorSuite()
    get_armored(a)

    b = IronMan()
    get_armored(b)