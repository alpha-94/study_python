
class Base:
    def __init__(self):
        print('Base')

class Derived(Base): # 지가 알아서 생성자를 만듬
    #def __init__(self):
    #    supper().__init__(self)
    pass


if __name__ == '__main__':
    d = Derived()
